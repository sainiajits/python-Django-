from django.shortcuts import render, redirect
from .models import Student
from student.form import studentForm
from django.contrib import messages
from django.contrib.auth.models import User, auth 
# Create your views here.

def home(request):
    return render(request, 'index.html')

def registration(request):
    return render(request, 'registration.html')

def instertData(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email'] 
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if Student.objects.filter(username=username).exists():
                messages.info(request, 'Username allready exists...')
                return redirect('registration')
            elif Student.objects.filter(email=email).exists():
                messages.info(request, 'Email allready exists...')
                return redirect('registration')
            else:
                insrt = Student(first_name=first_name, last_name=last_name, email=email, username=username, password=password2)
                insrt.save()
                messages.success(request, 'User Submit successfully...!')
                return redirect('all-records')
        else:            
            messages.error(request, 'Password does not match')
            return redirect('registration')
    else:
        return render(request, 'registration.html')

def fetchData(request):
    allRecords = Student.objects.all()
    return render(request, 'student.html', {"records":allRecords})

def editData(request, id):
    edit = Student.objects.get(id=id)
    return render(request, 'update.html', {"edit":edit})

def updateData(request, id):
    update = Student.objects.get(id=id)
    form = studentForm(request.POST, instance=update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Record updated successfully...!')   
        return render(request, 'update.html', {"edit":update})
    
def deleteData(request, id):
    delete = Student.objects.get(id=id)
    delete.delete()
    messages.success(request, 'Record Delete successfully...!')
    return redirect('all-records')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.success(request, 'Incorrect Username or password')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('/')
