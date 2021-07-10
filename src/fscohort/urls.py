from django.urls import path
from fscohort.views import home_page, student_add, student_list

urlpatterns = [
    path("", home_page, name="home_page"),
    path("list/", student_list, name="list"),
    path("add/", student_add, name="add")
]
