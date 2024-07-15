from django.shortcuts import render
from .models import People


# Create your views here.
def index(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('first_name')
        age = request.POST.get('age')
        email = request.POST.get('email')

        # create an object
        new_person = People(first_name=first_name, last_name=last_name, age=age, email=email)
        new_person.save()

        # get all persons-displays everything in the database.
    people = People.objects.all()
    return render(request, 'index.html', context={'people': people})
