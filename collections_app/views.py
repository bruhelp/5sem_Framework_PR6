from django.shortcuts import render

from models.paints_actions import get_paints_in_collection
from storage import load_collections, load_paints


def collections_list(request):
    """Показать список галерейных коллекций."""
    collections = load_collections("data/collections.json")
    context = {"collections": collections}
    return render(request, "collections/collection_list.html", context)


def collection_detail(request, collection_id):
    """Показать коллекцию и входящие в неё произведения."""
    collections = load_collections("data/collections.json")
    collection = next(
        (item for item in collections if item.id == collection_id),
        None,
    )
    collection_paints = []
    if collection is not None:
        paints = load_paints("data/paints.json", collections)
        collection_paints = get_paints_in_collection(
            paints,
            collection_id,
        )

    context = {
        "collection": collection,
        "paints": collection_paints,
    }
    return render(
        request,
        "collections/collection_detail.html",
        context,
        status=404 if collection is None else 200,
    )
