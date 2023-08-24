from django.shortcuts import render
from .forms import VolunteerForm
from .models import Volunteer

def register(request):
    if request.method == "POST":
        form = VolunteerForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VolunteerForm()
    return render(request, 'volunteer/form.html', {'form':form})


def detail(request, pk):
    volunteer = Volunteer.objects.get(pk=pk)
    if len(str(abs(volunteer.id))) == 4:
        zeros = ""
    elif len(str(abs(volunteer.id))) == 3:
        zeros = "0"
    elif len(str(abs(volunteer.id))) == 2:
        zeros = "00"
    elif len(str(abs(volunteer.id))) == 1:
        zeros = "000"
    volunteer.id = zeros + str(volunteer.id)
    return render(request, 'volunteer/detail.html', {'volunteer':volunteer})

def volunteers(request):
    volunteers = Volunteer.objects.all()
    for volunteer in volunteers:
        if len(str(abs(volunteer.id))) == 4:
            zeros = ""
        elif len(str(abs(volunteer.id))) == 3:
            zeros = "0"
        elif len(str(abs(volunteer.id))) == 2:
            zeros = "00"
        elif len(str(abs(volunteer.id))) == 1:
            zeros = "000"
        volunteer.id = zeros + str(volunteer.id)
    return render(request, 'volunteer/all.html', {'volunteer':volunteers})
    