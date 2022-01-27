from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Plan, Plan_Category

# Create your views here.

def view_plans(request):
    """ Show all Plans and sort/search queries """

    plans = Plan.objects.all()
    plan_categories = None

    if request.GET:
        if 'plan_category' in request.GET:
            plan_categories = request.GET['plan_category'].split(',')
            plans = plans.filter(plan_category__name__in=plan_categories)

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)


def plan_detail(request, plan_id):
    """ A View to show plan details """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan,
    }

    return render(request, 'plans/plan_detail.html', context)
