from django.shortcuts import render

from .models import Plan

# Create your views here.

def view_plans(request):
    """ Show all Plans and sort/search queries """

    plans = Plan.objects.all()

    context = {
        'plans': plans,
    }

    return render(request, 'plans/plans.html', context)
