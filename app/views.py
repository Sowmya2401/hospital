from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import Department, Doctor
from . forms import BookingForm
def index(request):
    department=Department.objects.all()
    doctor=Doctor.objects.all()
    form=BookingForm()
    context = {
        "department":department,
        "doctor":doctor,
        "form":form
    }
    if request.method=='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
    return render(request, "index.html", context)
def contact(request):
    return render(request, "contact.html")
