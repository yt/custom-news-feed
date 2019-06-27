from django.shortcuts import render

# Create your views here.


def home(request):
    template = 'home/home.html'

    if request.user.is_authenticated:
        print("User is logged in")
    else:
        print("User is not logged in")
        
    return render(request, template)
    