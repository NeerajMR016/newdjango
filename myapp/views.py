from django.shortcuts import render, redirect
from . models import Category, Product

# Create your views here.

def addproduct(request):
    d = {"categories":Category.objects.all()}
    if request.method == "POST":
        name = request.POST.get("name")
        desc = request.POST.get("desc")
        price = request.POST.get("price")
        quantity = request.POST.get("quantity")
        typed_category = request.POST.get("typed_category")
        selected_category = request.POST.get("selected_categpry")

        if typed_category:
            category, created = Category.objects.get_or_create(
                name = typed_category
            )
        else:
            category = Category.objects.get(id=selected_category)
        Product.objects.create(
            name = name,
            desc = desc,
            category = category,
            price = price,
            quantity = quantity
        )
        return redirect("product")
    return render(request, "addproduct.html", d)

def product(request):
    return render(request, "product.html")

def index(request):
    return render(request, "index.html")