from django.shortcuts import render, redirect
from .models import *
from django.db.models import Count

# Views to render templates here.
def index(request):
    return render(request,'main/index.html')

def dashboard(request):

    context = {
    "user" : User.objects.get(id = request.session["user_id"]),
    "targets" : User.objects.exclude(id = request.session["user_id"]),
    "hits" : Poke.objects.all().filter(victim=request.session["user_id"])
    }
    return render(request,'main/dashboard.html',context)


#Views to process forms under here
def register(request):
    if User.objects.validate_user(request.POST):
        user = User.objects.create(
        name = request.POST.get("name"),
        alias = request.POST.get("alias"),
        date_of_birth = request.POST.get("date_of_birth"),
        email = request.POST.get("email"),
        password = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
        )
        request.session["user_id"]=user.id
        return redirect("/dashboard")
    return redirect("/")

def login(request):
    if request.method == 'POST':
        login = User.objects.login_user(request.POST)
        if login:
            request.session["user_id"] = login[1].id
            return redirect ("/dashboard")
        else:
            messages.error(request,'Invalid credentials')
    return redirect("/")

def poke(request, id):
    aggressor = User.objects.get(id=request.session["user_id"])
    victim = User.objects.get(id=id)
    Poke.objects.filter()
    poke = Poke()
    poke.aggressor = aggressor
    poke.victim = victim
    poke.total+=1
    poke.save()
    return redirect('/dashboard')


def logout(request):
    request.session.clear()
    return redirect("/")
