from django.shortcuts import render, get_object_or_404, redirect
from news.models import News, Categories
from django.http import Http404
from news.forms import CreateCategoriesModelForm


# Create your views here.
def home(request):
    news = News.objects.all()
    context = {"news": news}
    return render(request, "home.html", context)


def news_details(request, id):
    try:
        news = get_object_or_404(News, id=id)
        context = {"news": news}
        return render(request, "news_details.html", context)
    except Http404:
        return render(request, "404.html")


def create_category(request):
    form = CreateCategoriesModelForm()

    if request.method == "POST":
        form = CreateCategoriesModelForm(request.POST)

        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")

    context = {"form": form}

    return render(request, "categories_form.html", context)
