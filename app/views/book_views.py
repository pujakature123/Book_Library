from django.shortcuts import render , redirect, HttpResponse
from app.models import Book



# Create your views here.

def welcome_page(request):
    return render(request, "welcome.html")

def show_active_book(request):
    book = Book.objects.filter(is_active=True)
    return render(request , "active_book.html", {"allbook":book})

def show_inactive_book(request):
    book = Book.objects.filter(is_active=False)
    return render(request , "inactive_book.html", {"allbook":book})

def show_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    return render (request, "bookdetail.html", {"book": book_obj})

def add_single_book(request):
    if request.method == "POST":
        final_dict = request.POST
        print(final_dict)
        book_name = final_dict.get("nm")
        book_price = final_dict.get("prc")
        book_qty = final_dict.get("qty")
        book_is_pub = final_dict.get("is_pub")
        if book_is_pub == "YES":
            is_pub = True
        else:
            is_pub = False
        
        Book.objects.create(name=book_name, price=book_price, qty=book_qty, is_publish=is_pub)
        return redirect("show_active_book")

        # print(request.POST)
        # print("in post method")  # checking its work or not
    elif request.method == "GET":
        return render (request , "addbook.html")

def edit_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    if request.method == "GET":
        return render(request, "editbook.html", {"single_book":book_obj})
    elif request.method == "POST":
        # print("In post method")
        final_dict = request.POST
        book_name = final_dict.get("nm")
        book_price = final_dict.get("prc")
        book_qty = final_dict.get("qty")
        book_is_pub = final_dict.get("is_pub")
        if book_is_pub =="YES":
            is_pub = True
        elif book_is_pub =="NO":
            is_pub = False

        # update data of book

        book_obj.name = book_name
        book_obj.price = book_price
        book_obj.qty = book_qty
        book_obj.is_pub = book_is_pub
        book_obj.save()

        return redirect("show_active_book")

def delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.delete()
    return redirect("show_active_book")

def soft_delete_single_book(request, bid):
    book_obj = Book.objects.get(id=bid)
    book_obj.is_active = False
    book_obj.save()
    return redirect("show_inactive_book")

