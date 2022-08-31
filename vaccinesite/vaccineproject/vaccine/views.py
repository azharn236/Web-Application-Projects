from django.contrib import messages
from django.shortcuts import render, redirect

from django.http import HttpResponse

# Create your views here.

from .models import Person
# Create your views here.


def vaccinePerson(request):
    persons = None
    persons = Person.objects.all()
    return render(request, 'home.html', {'persons': persons})
def details(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        gender = request.POST.get('gender', )
        age = request.POST.get('age', )
        date_of_birth = request.POST.get('date_of_birth',)
        mobile_no = request.POST.get('mobile_no',)
        persons = Person(name=name, gender=gender, age=age, date_of_birth=date_of_birth, mobile_no=mobile_no,)
        persons.save()
        personid = Person.objects.last()
        messages.info(request, "You have successfully vaccine booking.Your Id is:" +str(personid.id))
        return redirect('http://127.0.0.1:8000/details/')
    #     return redirect('/')
    return render(request, 'details.html')









