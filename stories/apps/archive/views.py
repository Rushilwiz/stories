from django.shortcuts import render, redirect

def landing(request):
    if request.user.is_authenticated:
        return redirect("home")
    else:
        return render(request, "pages/landing.html")