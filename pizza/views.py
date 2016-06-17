from django.shortcuts import render

from .models import Pizza


def index(request):
    """The homepage for Pizzeria"""
    return render(request, 'pizzas/index.html')
    
    
def pizzas(request):
    """Show all Pizzas."""
    pizzas =  Pizza.objects.order_by()
    context = {'pizzas': pizzas}
    return render(request, 'pizzas/pizza.html', context)
    
    
def pizza(request, pizza_id):
    """Show a single pizza and its toppings"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.order_by('-date_added')
    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizzs.html', context)
