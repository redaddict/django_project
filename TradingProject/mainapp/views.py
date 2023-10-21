from django.shortcuts import render
from mainapp.models import Nifty


# Create your views here.
def index(request):
    nifty = Nifty.objects.all()
    print(nifty)
    return render(request,'mainapp/index.html',{'nifty':nifty})
