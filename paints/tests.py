from django.test import Client, TestCase, override_settings


class GalleryPagesTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Система учёта работ художника")

    def test_paints_list_page(self):
        response = self.client.get("/paints/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Демон сидящий")

    def test_paint_detail_page(self):
        response = self.client.get("/paints/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Михаил Александрович Врубель")
        self.assertContains(response, "Масло")

    def test_unknown_paint_returns_404(self):
        response = self.client.get("/paints/999/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(response, "Работа не найдена", status_code=404)

    def test_collections_list_page(self):
        response = self.client.get("/collections/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Шедевры Государственной")

    def test_collection_detail_page(self):
        response = self.client.get("/collections/1/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Демон сидящий")

    def test_unknown_collection_returns_404(self):
        response = self.client.get("/collections/999/")
        self.assertEqual(response.status_code, 404)

    @override_settings(DEBUG=False)
    def test_unknown_url_uses_custom_404(self):
        response = self.client.get("/not-a-real-page/")
        self.assertEqual(response.status_code, 404)
        self.assertContains(
            response,
            "404 — страница не найдена",
            status_code=404,
        )
