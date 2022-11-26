from django.shortcuts import render, redirect
from .models import Subject, Lesson, Question
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def search_subject(request):
    sub_search = ""

    if request.GET.get("search"):
        sub_search = request.GET.get('search')

    subjects = Subject.objects.filter(Q(title__icontains = sub_search) | Q(description__icontains = sub_search))

    return subjects

@login_required(login_url="log-in")
def index(request):

    subjects = search_subject(request)

    return render(request, 'index.html', {"subjects" : subjects})

@login_required(login_url="log-in")
def subject(request, pk):

    subject = Subject.objects.get(id=pk)

    return render(request, 'subject.html', {"subject" : subject})

@login_required(login_url="log-in")
def list(request, pk):

    list = Lesson.objects.get(id=pk)

    return render(request, 'list.html', {"list" : list})

@login_required(login_url="log-in")
def excercise(request, pk):

    excercise = Lesson.objects.get(id=pk)

    return render(request, 'excercise.html', {"excercise" : excercise})

@login_required(login_url="log-in")
def test(request, pk):

    test = Lesson.objects.get(id=pk)

    return render(request, 'test.html', {"test" : test})

# AUTH
def loginUser(request):

    warning = {}

    if request.user.is_authenticated:
        return redirect("index")

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            warning = {"warning" : "Password or username are incorrect"}

    return render(request, "login.html", warning)

def logoutUser(request):
    logout(request)

    return redirect("log-in")
