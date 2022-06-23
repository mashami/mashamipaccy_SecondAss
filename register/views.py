from django.shortcuts import redirect, render
from django.urls import is_valid_path
from .models import *
from .form import *
from django.http import Http404, HttpResponse
# Create your views here.
def log_in (request):
     return render(request,"log_in.html")

def edit_Trainee(request,id):
    train=Tranees.objects.get(id=id)
  
    

    return render(request,"edit_Trainee.html",{'Edit':train})

def create_Trainee(request):
    if request.method=='POST':
        form=TraineesForms(request.POST)
        if form.is_valid():
            try:

                form.save()
                return redirect('/listAllTrainee')
            except:
                pass
    else :
        form=TraineesForms()

    return render(request,"create_Trainee.htm",{'create':form})


def listAllTrainee(request):
    Train = Tranees.objects.all()
    return render(request,"listAllTrainee.html",{'Tranees':Train})


def update_Trainee(request, id):
    train=Tranees.objects.get(id=id)
    form=TraineesForms(request.POST,instance=train)
    if form.is_valid():
        form.save()
        return redirect("/listAllTrainee")
    return render (request,"update_Trainee.html",{'update':train})


def delete_Trainee(request,id):
   
    try:
        train=Tranees.objects.get(id=id).delete()
        
    except Tranees.DoesNotExist:
        raise Http404("Trainee does not exist")
        
    return render(request,"delete_Trainee.html",{'Tranees':train})