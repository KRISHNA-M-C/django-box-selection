from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
from .services import recommend_box


def recommend_box_view(request):
    result = None

    if request.method == "POST":
        product = Product(
            name="Entered Product",
            length=float(request.POST["length"]),
            width=float(request.POST["width"]),
            height=float(request.POST["height"]),
            weight=float(request.POST["weight"]),
        )

        box = recommend_box(product)

        if box:
            result = f"Recommended Box: {box.name} | Cost: {box.cost}"
        else:
            result = "No suitable box found."

    return render(
        request,
        "box_selectors/recommend.html",
        {"result": result}
    )