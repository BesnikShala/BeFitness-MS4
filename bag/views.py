from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product
from plans.models import Plan

# Create your views here.

def view_bag(request):
    """ A View to render the checkout bag """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add products and quantity to the bag """
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    item_type = redirect_url.split("/")[1]
    bag = request.session.get('bag', {"products": {}, "plans": {}})

    if item_type == "products":
        product = get_object_or_404(Product, pk=item_id)
        if item_id in list(bag['products'].keys()):
            bag['products'][item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag["products"][item_id]}')
        else:
            bag['products'][item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')
    elif item_type == "plans":
        plan = get_object_or_404(Plan, pk=item_id)
        if item_id in list(bag['plans'].keys()):
            bag['plans'][item_id] += quantity
            messages.success(request, f'Added {plan.name} to your bag')
        else:
            bag['plans'][item_id] = quantity
            messages.success(request, f'Added {plan.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, item_id):
    """ Remove item from bag """

    try:
        product = None
        plan = None
        bag = request.session.get('bag', {"product": {}, "plan": {}})
        item_type = request.POST['item_type']

        if 'item_type' in request.POST:
            item_type = request.POST['item_type']

        if item_type == 'product':
            product = get_object_or_404(Product, pk=item_id)
            if item_id in bag["products"].keys():
                del bag['products'][item_id]
            messages.success(request, f'Removed {product.name} from your bag')
        elif item_type == 'plan':
            plan = get_object_or_404(Plan, pk=item_id)
            if item_id in bag["plans"].keys():
                del bag['plans'][item_id]
            messages.success(request, f'Removed {plan.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error Removing item: {e}')
        return HttpResponse(status=500)

