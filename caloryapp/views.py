from django.shortcuts import render, redirect
from . models import Food, Consume
# Create your views here.


def index(request):
    if request.method == "POST":
        food_consume = request.POST['food_consume']
        consume = Food.objects.get(name=food_consume)
        user = request.user
        consume = Consume(user=user, food_consume=consume)
        consume.save()
        foods = Food.objects.all()
    
    else:
        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'caloryapp/index.html', {
        'foods':foods, 
        'consumed_food':consumed_food
        })


def delete_consume(request, id):
    consume_food = Consume.objects.get(id=id)
    if request.method == "POST":
        consume_food.delete()
        return redirect('/')
    return render(request, 'caloryapp/delete.html')