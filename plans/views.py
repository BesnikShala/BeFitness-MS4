
from django.shortcuts import render, get_object_or_404

from .models import Plan

# Create your views here.

def view_plans(request):
    """ Show all Plans and sort/search queries """

    plans = Plan.objects.all()

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
