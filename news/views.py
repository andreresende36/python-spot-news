from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Categories, Users
from .forms import CategoryForm, NewsForm


def home(request):
    news_list = News.objects.all()
    context = {
        "news_list": news_list,
    }
    return render(request, "home.html", context)


def news_details(request, id):
    news = get_object_or_404(News, id=id)
    return render(request, "news_details.html", {"news": news})


def categories_form(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home-page")
    else:
        form = CategoryForm()
    return render(request, "categories_form.html", {"form": form})


def news_form(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "home-page"
            )
    else:
        form = NewsForm()

    users = Users.objects.all()
    categories = Categories.objects.all()

    context = {
        "form": form,
        "users": users,
        "categories": categories,
    }

    return render(request, "news_form.html", context)
