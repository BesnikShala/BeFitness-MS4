from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Plan, Plan_Category
from .forms import PlanForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def view_plans(request):
    """ Show all Plans and sort/search queries """

    plans = Plan.objects.all()
    plan_categories = None

    if request.GET:
        if 'plan_category' in request.GET:
            plan_categories = request.GET['plan_category'].split(',')
            plans = plans.filter(plan_category__name__in=plan_categories)
            plan_categories = Plan_Category.objects.filter(name__in=plan_categories)

    context = {
        'plans': plans,
        'current_categories': plan_categories
    }

    return render(request, 'plans/plans.html', context)


def plan_detail(request, plan_id):
    """ A View to show plan details """

    plan = get_object_or_404(Plan, pk=plan_id)

    context = {
        'plan': plan, 
    }

    return render(request, 'plans/plan_detail.html', context)


@login_required
def add_plan(request):
    """ Add a plan """
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only admin has access to this')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES)
        if form.is_valid():
            plan = form.save()
            messages.success(request, 'Successfully added plan')
            return redirect(reverse('plan_detail', args=[plan.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = PlanForm()

    template = 'plans/add_plan.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
