from django.shortcuts import render,redirect
from django.http import HttpResponse
from . import models
from datetime import datetime,timedelta
# Create your views here.
class test:
    ob=models.Data() 
cobj=test()
def home(request):
    return render(request,'home.html')

def input(request):
    note,name=request.POST['note'],request.POST['name']
    obj=models.Data()
    obj.note_text=note
    obj.moment=datetime.utcnow()+timedelta(hours=5.5)
    obj.name=name
    obj.save()
    return redirect('home')
    


def create(request):
    return render(request,'input.html')

def view(request):
    obj=models.Data.objects.order_by('-moment')
    
    #obj1=obj.order_by(models.Data.moment)
    #print(obj1)
    return render(request,'view.html',{'object':obj})    

#def delete(request):
 #   return HttpResponse('hello') 
#def abcd(request):
 #   return HttpResponse('hello')
def tru(request,note,time):
    obj=models.Data.objects.get(note_text=note,moment=time)
    obj.delete()
    print(obj)
    return redirect('view')


def edit(request,note,time):
    obj=models.Data.objects.get(note_text=note,moment=time)
    cobj.ob=obj
    return render(request,'edit.html',{'object':obj})
    
def editsave(request,note,time):
    obj1=cobj.ob
    print(obj1)
    note,name=request.POST['note'],request.POST['name']
    obj1.note_text=note
    obj1.name=name
    obj1.save()
    return redirect('view')

