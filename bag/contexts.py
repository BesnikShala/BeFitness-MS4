from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from plans.models import Plan


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    plan_count = 0
    bag = request.session.get('bag', {"products": {}, "plans": {}})
    plan = None
    product = None 

    for key, value in bag.items():
        for item_id, item_data in bag[key].items():
            if key == "products":
                product = get_object_or_404(Product, pk=item_id)
                total += item_data * product.price
                product_count += item_data
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'product': product,
                })
            elif key == "plans":
                plan = get_object_or_404(Plan, pk=item_id)
                total += item_data * plan.price
                plan_count += item_data
                bag_items.append({
                    'item_id': item_id,
                    'quantity': item_data,
                    'plan': plan,
                })
            else:
                product = get_object_or_404(Product, pk=item_id)
                for size, quantity in item_data['items_by_size'].items():
                    total += quantity * product.price
                    product_count += quantity
                    bag_items.append({
                        'item_id': item_id,
                        'quantity': quantity,
                        'product': product,
                        'size': size,
                    })

    grand_total = total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'plan_count': plan_count,
        'grand_total': grand_total,
    }

    return context
