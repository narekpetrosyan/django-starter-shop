from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from item.models import Item, Category
from item.forms import NewItemForm, EditItemForm


def items(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', 0)
    items = Item.objects.filter(is_sold=False)
    categories = Category.objects.filter()

    if category_id:
        items = items.filter(category=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) |
                             Q(description__icontains=query))

    return render(request, "items.html", {
        "query": query,
        "category_id": int(category_id),
        "items": items,
        "categories": categories,
    })


def show(request, id):
    item = get_object_or_404(Item, id=id)
    related_items = Item.objects.filter(
        category=item.category, is_sold=False).exclude(id=id)[:3]

    return render(request, "show.html", {
        "item": item,
        "related_items": related_items
    })


@login_required
def create_item(request):
    if request.method == "POST":
        form = NewItemForm(request.POST, request.FILES)

        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect("item:show", id=item.id)

    form = NewItemForm()
    return render(request, "form.html", {
        "title": "Create item",
        "form": form
    })


@login_required
def edit_item(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=item)

        if form.is_valid():
            form.save()
            return redirect("item:show", id=item.id)

    form = EditItemForm(instance=item)
    return render(request, "form.html", {
        "title": "Edit item",
        "form": form
    })


@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, id=id, created_by=request.user)
    item.delete()
    return redirect("dashboard:index")
