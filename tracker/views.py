from django.shortcuts import render
from .models import Consume, Food

# Create your views here.
def index(request):
    
    if request.method == 'POST':
        food_consumed = request.POST['foodConsumed']
        consume = Food.objects.get(pk=food_consumed)
        user = request.user
        
        consume = Consume(food=consume, user=user)
        consume.save()
        
    elif request.method == 'GET' and 'delete' in request.GET:
        id = request.GET['delete']
        
        try:
            consumed_food = Consume.objects.get(pk=id)
        except Consume.DoesNotExist:
            consumed_food = None
        if consumed_food and consumed_food.user == request.user:
            consumed_food.delete()
        
    consumed_food = Consume.objects.filter(user=request.user)
    foods = Food.objects.all()    
    
    context = {
        'foods': foods,
        'consumed_food': consumed_food,
    }
    
    return render(request, 'tracker/index.html', context)


def delete_consume(request, id):
    consumed_food = Consume.objects.get(pk=id)
    consumed_food.delete()
    
    return render(request, 'tracker/index.html')