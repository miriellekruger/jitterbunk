from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404, render
from bunk.models import User, Bunk
from django.urls import reverse
from django.contrib.auth.models import User as AuthUser


def index(request):
    all_bunks = Bunk.objects.order_by("-time")
    return render(request, "bunk/index.html", {"all_bunks": all_bunks,})

def detail(request, pk):
    bunk = get_object_or_404(Bunk, pk=pk)
    return render(request, "bunk/detail.html", {"bunk": bunk,})

def personalBunk(request, pk):
    current_user = get_object_or_404(User, pk=pk)
    my_from_bunks = Bunk.objects.filter(from_user=pk).order_by("-time")
    my_to_bunks = Bunk.objects.filter(to_user=pk).order_by("-time")
    return render(request, "bunk/user.html", {"current_user":current_user,"my_from_bunks": my_from_bunks, "my_to_bunks":my_to_bunks})

def bunker(request):
    user_list = get_list_or_404(User.objects.order_by("username"))
    return render(request, "bunk/bunker.html", {"user_list": user_list,})

def bunkerSubmit(request):
    users = User.objects.all()
    try:
        selected_from_user = users.get(pk=request.POST["from_user"])
        selected_to_user = users.get(pk=request.POST["to_user"])

    except (KeyError, User.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "bunk/bunker.html",
            {
                "error_message": "You didn't select a user.",
            },
        )
    else:
        bunk = Bunk.objects.create(from_user=selected_from_user, to_user= selected_to_user)
        bunk.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("index"))
    
def signup(request):
    image_list = ["bunk/images/buggo_profile.png","bunk/images/ghost_profile.png","bunk/images/tracy_profile.png","bunk/images/karel_profile.png",]
    return render(request, "registration/signup.html", {"image_list":image_list})

def signup_submit(request):
    try:
        username = request.POST["username"]
        photo = request.POST["photo"]
        password = request.POST["password"]

    except (KeyError, User.DoesNotExist or AuthUser.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "bunk/signup.html",
            {
                "error_message": "You didn't fill out the form fully.",
            },
        )
    else:
        authuser = AuthUser.objects.create_user(username=username, password=password)
        authuser.save()
        user = User.objects.create(username=username, photo=photo, auth_user=authuser)
        user.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("login"))
    

