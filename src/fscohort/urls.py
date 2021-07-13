from django.urls import path
from fscohort.views import home_page, student_add, student_delete, student_detail, student_list, student_update

urlpatterns = [
    path("", home_page, name="home"),
    path("list/", student_list, name="list"),
    path("add/", student_add, name="add"),
    path('<int:id>/', student_detail, name="detail"),
    path('<int:id>/update/', student_update, name="update"),
    path('<int:id>/delete/', student_delete, name="delete"),
]
