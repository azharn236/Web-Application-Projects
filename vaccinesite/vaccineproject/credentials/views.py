from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# from vaccineproject.vaccine.models import Person


def login(request):
    if request.method=='POST':
        username = request.POST['Username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('http://127.0.0.1:8000/details/')
            # return redirect('/')
        else:
            messages.info(request, "Invalid credentials or not a registered user")
            return redirect('http://127.0.0.1:8000/credentials/login/')
            # return redirect('login')
    return render(request, 'login.html')
def register(request):
    if request.method=='POST':
        username = request.POST['Username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('http://127.0.0.1:8000/credentials/register/')
            elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email ID Taken")
                    return redirect('http://127.0.0.1:8000/credentials/register/')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=first_name, last_name=last_name, email=email)
                user.save();
                return redirect('http://127.0.0.1:8000/credentials/login/')
        else:
            messages.info(request, "password not matching")
            return redirect('http://127.0.0.1:8000/credentials/register/')
        return redirect('/')
    return render(request, 'register.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
# def details(request):
#     if request.method == "POST":
#         name = request.POST.get('name', )
#         gender = request.POST.get('gender', )
#         age = request.POST.get('age', )
#         date_of_birth = request.POST.get('date_of_birth',)
#         mobile_no = request.POST.get('mobile_no',)
#         persons = Person(name=name, gender=gender, age=age, date_of_birth=date_of_birth, mobile_no=mobile_no,)
#         persons.save()
#         return redirect('http://127.0.0.1:8000/details/')
#     return render(request, 'details.html')