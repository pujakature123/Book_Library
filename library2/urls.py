"""
URL configuration for library2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.urls import path

from app.views.book_views import welcome_page, show_active_book, show_inactive_book, show_single_book, add_single_book, edit_single_book, delete_single_book,soft_delete_single_book
# from app.views.file_views import create_csv, create_excle , upload_csv ----  second way to import
from app.views import file_views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/", welcome_page, name="welcome_page"), 
    path("all-active-book/", show_active_book, name="show_active_book"),
    path("all-inactive-book/", show_inactive_book, name="show_inactive_book"),
    path("book-detail/<int:bid>/", show_single_book, name="show_single_book"),
    path("add-book/", add_single_book, name="add_single_book"),
    path("edit-book/<int:bid>/", edit_single_book, name="edit_single_book"),
    path("delete-book/<int:bid>/", delete_single_book, name="delete_single_book"),
    path("soft-delete-book/<int:bid>/", soft_delete_single_book, name="soft_delete_single_book"), 


    # file export ----------
    
    path("create-csv/", file_views.create_csv, name="create_csv"),
    path("create-excle/", file_views.create_excle, name="create_excle"),
    path("upload-csv/", file_views.upload_csv, name="upload_csv"),
    	
   

]


# http://127.0.0.1:8000/home/
# http://127.0.0.1:8000/all-active-book/
# http://127.0.0.1:8000/all-inactive-book/
# http://127.0.0.1:8000/book-detail/<int:bid>/
# http://127.0.0.1:8000/add-book/
# http://127.0.0.1:8000/edit-book/<int:bid>/
# http://127.0.0.1:8000/delete-book/<int:bid>/
# http://127.0.0.1:8000/soft-delete-book/<int:bid>/
# http://127.0.0.1:8000/create-csv/
# http://127.0.0.1:8000/create-excle/
# http://127.0.0.1:8000/upload-csv/

