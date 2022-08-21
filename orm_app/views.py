from django.shortcuts import render
from .models import Room

# from django.http import  HttpResponse

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Front end developer'},
    {'id': 2, 'name': 'Front end designer'},
    {'id': 3, 'name': 'Front end tester'},
]
def home(request):
    rooms=Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'orm_app/home.html', context)


def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'orm_app/room.html', context)
