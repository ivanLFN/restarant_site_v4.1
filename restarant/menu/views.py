from django.shortcuts import render
from .models import MenuPosition

def menu_home(request):
    # positions = MenuPosition.objects.all()[:1]
    # positions = MenuPosition.objects.all()
    # fast_food = MenuPosition.objects.filter(tag='fast-food')
    fast_food = MenuPosition.objects.filter(tag='fast-food')
    pizzas = MenuPosition.objects.filter(tag='pizza')

    return render(request, 'menu.html', {'fast_food': fast_food, 'pizzas': pizzas})
