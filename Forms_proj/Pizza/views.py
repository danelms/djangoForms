from django.shortcuts import render
from Pizza.forms import PizzaOrderForm

def home(request):
    return render(request, 'home.html')
    
def order(request):

    if request.method == 'POST':
        filled_form = PizzaOrderForm(request.POST)
        if filled_form.is_valid():
            message = 'Thanks for your order, your %s %s and %s pizza is on its way!' % (filled_form.cleaned_data['size'], filled_form.cleaned_data['topping1'], filled_form.cleaned_data['topping2'])
            new_form = PizzaOrderForm()
            return render(request, 'order.html', {'pizzaOrderForm': new_form, 'message': message})
    else:
        orderForm = PizzaOrderForm()
        
    return render(request, 'order.html', {'pizzaOrderForm': PizzaOrderForm})