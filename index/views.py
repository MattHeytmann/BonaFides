from django.shortcuts import render, redirect
from .models import Subject, Lesson, PrivateSubject, PrivateLesson, PrivateQuestion
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def search_subject(request, sub):
    sub_search = ""

    if request.GET.get("search"):
        sub_search = request.GET.get('search')

    subjects = sub.objects.filter(Q(title__icontains = sub_search) | Q(description__icontains = sub_search))

    return subjects

@login_required(login_url="log-in")
def index(request):

    user = request.user

    subjects = search_subject(request, Subject)
    privateSubjects = search_subject(request, PrivateSubject).filter(author = user)

    return render(request, 'index.html', {"subjects" : subjects, "privateSubjects": privateSubjects, "address" : "index"})

@login_required(login_url="log-in")
def subject(request, pk):

    subject = Subject.objects.get(id=pk)
    return render(request, 'subject.html', {"subject" : subject, "address" : "index"})

@login_required(login_url="log-in")
def privateSubject(request, pk):
    
    user = request.user
    subject = PrivateSubject.objects.filter(author = user).get(id=pk)

    return render(request, 'privateSubject.html', {"subject" : subject, "address" : "index"})


@login_required(login_url="log-in")
def llist(request, pk):

    llist = Lesson.objects.get(id=pk)

    return render(request, 'list.html', {"list" : llist, "address" : 'subject', "num" : llist.subject.id})

@login_required(login_url="log-in")
def excercise(request, pk):

    excercise = Lesson.objects.get(id=pk)

    return render(request, 'excercise.html', {"excercise" : excercise, "address" : "subject", "num" : excercise.subject.id})

@login_required(login_url="log-in")
def test(request, pk):

    test = Lesson.objects.get(id=pk)

    return render(request, 'test.html', {"test" : test, "address" : "subject", "num" : test.subject.id})

# PRIVATE
@login_required(login_url="log-in")
def privateList(request, pk):

    llist = PrivateLesson.objects.get(id=pk)

    context = {
        "list" : llist, 
        "address" : "privateSubject",
        "num" : llist.subject.id,
    }

    if request.method == "POST":
        
        try:
            PrivateQuestion.objects.create(
                lesson = llist,
                title = request.POST.get("assigment"),
                description = request.POST.get("description"),
                answer = request.POST.get("answer"),
            )
            return redirect(f"/privateList/{llist.id}")
        except:
            context['message'] = "invalid details"

    return render(request, 'privateList.html', context)

@login_required(login_url="log-in")
def privateExcercise(request, pk):

    excercise = PrivateLesson.objects.get(id=pk)

    return render(request, 'privateExcercise.html', {"excercise" : excercise, "address" : "privateSubject", "num" : excercise.subject.id})

@login_required(login_url="log-in")
def privateTest(request, pk):

    test = PrivateLesson.objects.get(id=pk)

    return render(request, 'privateTest.html', {"test" : test, "address" : "privateSubject", "num" : test.subject.id})

@login_required(login_url='log-in')
def privateSubjectCreate(request):

    context = {"address" : "index"}

    if request.method == "POST":
        
        try:
            PrivateSubject.objects.create(
                title = request.POST.get("subjectName"),
                description = request.POST.get("subjectDescription"),
                author = request.user
            )
            return redirect("index")
        except:
            context['message'] = "invalid details"

        
    return render(request, 'createPrivateSubject.html', context)

@login_required(login_url='log-in')
def privateLessonCreate(request, pk):

    subject = PrivateSubject.objects.get(id = pk)

    context = {
        'sub' : subject, 
        "address" : "privateSubject", 
        "num" : subject.id
    }

    if request.method == "POST":
        
        try:
            PrivateLesson.objects.create(
                subject = subject,
                title = request.POST.get("subjectName"),
                description = request.POST.get("subjectDescription"),
                author = request.user
            )
            return redirect(f"/privateSubject/{subject.id}")
        except:
            context['message'] = "invalid details"

        
    return render(request, 'createPrivateLesson.html', context)

# AUTH
def loginUser(request):

    warning = {"address" : "index"}

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
            warning["warning"] = "Password or username are incorrect"

    return render(request, "login.html", warning)

def logoutUser(request):
    logout(request)

    return redirect("log-in")

# DELETE

@login_required(login_url='log-in')
def deleteSubject(request, pk):

    subject = PrivateSubject.objects.get(id=pk)

    subject.delete()

    return redirect("index")

@login_required(login_url='log-in')
def deleteLesson(request, pk):

    lesson = PrivateLesson.objects.get(id=pk)

    lesson.delete()

    return redirect(f"/privateSubject/{lesson.subject.id}")

@login_required(login_url='log-in')
def deleteQuestion(request, pk):

    question = PrivateQuestion.objects.get(id=pk)
    lesson = question.lesson

    question.delete()

    return redirect(f"/privateList/{lesson.id}")