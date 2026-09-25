from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import admission
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect



@login_required
def home(request):
    return render(request, "home.html")

def login(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        print(user) 

        if user is not None:
            auth_login(request, user)
            return redirect("home")

        else:
            return render(request, "login.html", {
                "error": "Invalid username or password"
            })

    return render(request, "login.html")


def home(request):

    return render(request, "home.html")
def logout_view(request):

    logout(request)

    return redirect("login")

@ login_required
def admission_form(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        course = request.POST.get("course")
        date_of_birth = request.POST.get("date_of_birth")
        address = request.POST.get("address")

        admission.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            course=course,
            date_of_birth=date_of_birth,
            address=address
        )


    return render(request, "admission.html")
@login_required
def stu_details(request):

    admissions = admission.objects.all()

    return render(request, "stu_details.html", {
        "admissions": admissions
    })



def delete_student(request, id):

    student = get_object_or_404(admission, id=id)

    student.delete()

    return redirect("stu_details")


def update_student(request, id):

    student = get_object_or_404(admission, id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.email = request.POST.get("email")
        student.phone_number = request.POST.get("phone_number")
        student.course = request.POST.get("course")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.address = request.POST.get("address")

        student.save()

        return redirect("stu_details")

    return render(request, "update_student.html", {
        "student": student
    })
