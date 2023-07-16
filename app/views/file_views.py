import csv
from app.models import Book
from django.shortcuts import HttpResponse, redirect, render
import xlwt
# export csv ----

def create_csv(request):
    response = HttpResponse(content_type ='text/csv')
    response['Content-Disposition'] = 'attachment; filename="test.csv"'

    writer = csv.writer(response)
    writer.writerow(["name", "price", "qty", "is_publish", "is_active"])

    books = Book.objects.all().values_list("name", "price", "qty", "is_publish", "is_active")
    for book in books:
        writer.writerow(book)

    return response

def create_excle(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="book.xls"'
    
    workbook= xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('Active_book')

    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    row_num = 0
    
    headers = ["name", "price", "qty", "is_publish", "is_active"]
    # # import pdb;pdb.set_trace()  #--------------- debuger

    for col_num in range(len(headers)):
        worksheet.write(row_num, col_num, headers[col_num], font_style)

    font_style = xlwt.XFStyle()

    books = Book.objects.all().values_list("name", "price", "qty", "is_publish", "is_active")
    for book in books:
        row_num += 1
        for col_num in range(len(book)):
            worksheet.write(row_num, col_num, book[col_num], font_style)

    workbook.save(response)
    return response

#uploading csv file ----
def upload_csv(request):
    file = request.FILES["csv_file"]
    data = file.read().decode('utf-8').splitlines()
    print(data)    # ['name,price,qty,is_publish,is_active', 'Sanskrit,200,2,True,True', 'English,600,23,True,False']

    # here we apply validations if headers are diffrent 
    expected_headers_lst = ["name", "price", "qty", "is_publish", "is_active"]  
    expected_headers_lst.sort() 
    actual_headers_lst = data[0].split(",")
    actual_headers_lst.sort()
    print(expected_headers_lst , actual_headers_lst)   # for checking  ['is_active', 'is_publish', 'name', 'price', 'qty'] [' quantity', 'is_publish', 'name', 'price']
    if expected_headers_lst != actual_headers_lst:
        return HttpResponse ("Error...Headers are not equal..!")

    reader = csv.DictReader(data)    # always use DictReader (incase we use reader then values in form of tuple of tuple and in sence values sequence might be change then it gives error )
    lst = []
    for item in reader:
        is_pub = item.get("is_publish") # here we get is_pub is true or false
        if is_pub == "TRUE":
            is_pub = True
        else:
            is_pub = False
        lst.append(Book(name=item.get("name"), price=item.get("price"), qty=item.get("qty"), is_publish=is_pub))   # must use this way 
        # lst.append(Book(name=item["name"], price=item["price"], qty=item["qty"], is_publish=is_pub)) # we can also write it but value is none(not_mention ) then it gives error

    Book.objects.bulk_create(lst)  # here we pass that lst where we append writing data
    return HttpResponse("Success")


    