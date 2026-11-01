from django.shortcuts import render

from models.paints_actions import find_paint_by_id, sort_paints_by_year
from storage import load_collections, load_paints


def _get_paints():
    """Загрузить картины вместе с коллекциями из JSON-хранилища."""
    collections = load_collections("data/collections.json")
    return load_paints("data/paints.json", collections)


def paints_list(request):
    """Показать каталог работ с сортировкой по году создания."""
    paints = sort_paints_by_year(_get_paints())
    context = {
        "paints": paints,
        "page_title": "Каталог произведений",
    }
    return render(request, "paints/paint_list.html", context)


def paint_detail(request, paint_id):
    """Показать сведения о работе или вернуть страницу 404."""
    paint = find_paint_by_id(_get_paints(), paint_id)
    context = {"paint": paint}
    return render(
        request,
        "paints/paint_detail.html",
        context,
        status=404 if paint is None else 200,
    )
