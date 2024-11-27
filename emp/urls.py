from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path("home/",emp_home, name='home'),
    path("add-emp/",add_emp, name='add-emp'),
    path("delete-emp/<int:emp_id>",delete_emp),
    path("update-emp/<int:emp_id>",update_emp),
    path("do-update-emp/<int:id>",do_update_emp),
    path("view-emp/<int:id>", view_emp, name='view-emp'),
    path("search/", search, name='search'),
]
