from django.shortcuts import redirect, render
from django.http import HttpResponse
from fscohort.forms import StudentForm
from fscohort.models import Student
# Create your views here.

# def home(request):
#     return HttpResponse("This is home page")

def home_page(request):
    return render(request, "fscohort/home.html")

def student_list(request):
    students = Student.objects.all()

    context = {
        "students": students
    }

    return render(request, "fscohort/student_list.html", context)

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

# def student_detail(request):
