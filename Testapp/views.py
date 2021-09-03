from django.shortcuts import render,redirect
from Testapp.models import Student
from Testapp.forms import StudentForm
# Create your views here.
def show_view(request):
    student=Student.objects.all().order_by('no')
    return render(request,'html/index.html',{'student':student})

def insert_view(request):
    form=StudentForm()
    if request.method == 'POST':
        form=StudentForm(request.POST)
        if form.is_valid():
           form.save()
        return redirect('/')
    return render(request,'html/insert.html',{'form':form})

def update_view(request,id):
   if request.method=='POST':
       student=Student.objects.get(id=id)
       form=StudentForm(request.POST,instance=student)
       if form.is_valid():
          form.save()
       return redirect('/')
   else:
       student=Student.objects.get(id=id)
       form=StudentForm(instance=student)
   return render(request,'html/update.html',{'form':form})

def delete_view(request,id):
    student=Student.objects.get(id=id)
    return render(request,'html/del.html',{'student':student})

def del_view(request,id):
    student=Student.objects.get(id=id)
    student.delete()
    return redirect('/')
