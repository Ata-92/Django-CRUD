from django.shortcuts import get_object_or_404, redirect, render
# from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from fscohort.forms import StudentForm
from fscohort.models import Student
from django.urls import reverse_lazy

# Create your views here.

# def home(request):
#     return HttpResponse("This is home page")

def home_page(request):
    return render(request, "fscohort/home.html")

class HomeView(TemplateView):
    template_name = "fscohort/home.html"

def student_list(request):
    students = Student.objects.all()

    context = {
        "students": students
    }

    return render(request, "fscohort/student_list.html", context)

class StudentList(ListView):
    model = Student
    # template_name  # default  "app/modelName.lower()_list.html" = "fscohort/student_list.html"
    context_object_name = "students"  # default object_list
    # ordering = ["num"]
    paginate_by = 2

def student_add(request):
    form = StudentForm()
    if request.method == "POST":
        print(request.POST)
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
    context = {
        "form": form
    }
    return render(request, "fscohort/student_add.html", context)

class StudentAdd(CreateView):
    model = Student
    # fields = ("first_name", "last_name", "number")
    form_class = StudentForm
    template_name = "fscohort/student_add.html"  # default  "app/modelName.lower()_form.html" = "fscohort/student_form.html"
    success_url = reverse_lazy("list") # "/list/"

def student_detail(request, id):
    student = Student.objects.get(id=id)
    context = {
        "student": student
    }
    return render(request, "fscohort/student_detail.html", context)

class StudentDetail(DetailView):
    model = Student
    pk_url_kwarg = "id"  #  default  "pk or "slug"
    # template_name  #  default "app/modelName.lower()_detail.html" = "fscohort/student_detail.html"

def student_update(request, id):
    # student = Student.objects.get(id=id)
    student = get_object_or_404(Student, id=id)
    # form = StudentForm(instance=student)
    # if request.method == "POST":
    #     form = StudentForm(request.POST, instance=student)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect("list")

    context = {
        "student": student,
        "form": form
    }

    return render(request, "fscohort/student_update.html", context)

class StudentUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = "fscohort/student_update.html"  #  default  "app/modelName.lower()_form.html" = "fscohort/student_form.html"
    success_url = "/list/"  #  reverse_lazy("list")

def student_delete(request, id):
    student = get_object_or_404(Student, id=id)
    if request.method == "POST":
        student.delete()
        return redirect("list")

    context = {
        "student": student
    }

    return render(request, "fscohort/student_delete.html", context)

