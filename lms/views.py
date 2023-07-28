from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Author, Book, Category

last_query = ""


def filter_categories(request):
    global last_query
    query = request.GET.get("q", last_query)
    last_query = query
    categories = Category.objects.filter(type__icontains=query)

    filtered_categories = [category for category in categories]
    for category in Category.objects.all():
        if (
            category.books.filter(title__icontains=query)
            and category not in filtered_categories
        ):
            filtered_categories.append(category)

        for book in category.books.all():
            if (
                book.author.filter(name__icontains=query)
                and category not in filtered_categories
            ):
                filtered_categories.append(category)

    return filtered_categories


# Create your views here.
def index(request):
    global last_query
    filtered_categories = filter_categories(request)
    context = {
        "categories": filtered_categories,
        "query": last_query,
        "is_home": True,
    }
    return render(request, "lms/index.html", context)


def view_book(request, book_id):
    filtered_categories = filter_categories(request)
    book = Book.objects.get(pk=book_id)
    context = {
        "categories": filtered_categories,
        "book": book,
        "is_viewing": True,
    }
    return render(request, "lms/index.html", context)


def add_book(request):
    filtered_categories = filter_categories(request)
    authors = Author.objects.all()

    if request.method == "POST":
        authors = request.POST.getlist("book_author")
        categories = request.POST.getlist("book_categories")
        book = Book(
            title=request.POST["book_title"],
            description=request.POST["book_description"],
            pages=request.POST["book_pages"],
        )
        book.save()
        book.author.set(Author.objects.filter(name__in=authors))
        book.category_set.set(Category.objects.filter(type__in=categories))
        return redirect(reverse("lms:index"))

    context = {
        "categories": filtered_categories,
        "is_adding": True,
        "authors": authors,
    }
    return render(request, "lms/index.html", context)


def update_book(request, book_id):
    filtered_categories = filter_categories(request)
    book = Book.objects.get(pk=book_id)

    if request.method == "POST":
        new_authors = request.POST.getlist("book_author")
        new_categories = request.POST.getlist("book_categories")

        book.title = request.POST["book_title"]
        book.description = request.POST["book_description"]
        book.pages = request.POST["book_pages"]

        book.author.set(Author.objects.filter(name__in=new_authors))
        book.category_set.set(Category.objects.filter(type__in=new_categories))
        book.save()
        return redirect(reverse("lms:index"))

    authors = Author.objects.all()
    context = {
        "categories": filtered_categories,
        "book": book,
        "authors": authors,
        "is_updating": True,
    }
    return render(request, "lms/index.html", context)


def edit_category(request):
    filtered_categories = filter_categories(request)
    all_books = Book.objects.all()

    if request.method == "POST":
        type = request.POST["option"]
        books = request.POST.getlist("books")
        category, _ = Category.objects.get_or_create(type=type)
        category.books.set(Book.objects.filter(title__in=books))
        category.save()
        return redirect(reverse("lms:index"))

    context = {
        "label": "Category",
        "categories": filtered_categories,
        "books": all_books,
        "is_editing": True,
    }
    return render(request, "lms/index.html", context)


def edit_author(request):
    filtered_categories = filter_categories(request)
    authors = Author.objects.all()
    all_books = Book.objects.all()

    if request.method == "POST":
        name = request.POST["option"]
        books = request.POST.getlist("books")
        author, _ = Author.objects.get_or_create(name=name)
        author.book_set.set(Book.objects.filter(title__in=books))
        author.save()
        return redirect(reverse("lms:index"))

    context = {
        "label": "Author",
        "categories": filtered_categories,
        "authors": authors,
        "books": all_books,
        "is_editing": True,
    }
    return render(request, "lms/index.html", context)


def archive_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.is_archived = True
    book.save()
    return redirect(reverse("lms:index"))
