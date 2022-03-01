from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Plan, Plan_Category
from .forms import PlanForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def view_plans(request):
    """ Show all Plans and sort/search queries """

    plans = Plan.objects.all()
    plan_categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                plans = plans.annotate(lower_name=Lower('name'))
            if sortkey == 'plan_category':
                sortkey = 'plan_category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            plans = plans.order_by(sortkey)

        if 'plan_category' in request.GET:
            plan_categories = request.GET['plan_category'].split(',')
            plans = plans.filter(plan_category__name__in=plan_categories)
            plan_categories = Plan_Category.objects.filter(name__in=plan_categories)

    current_sorting = f'{sort}_{direction}'

    context = {
        'plans': plans,
        'current_categories': plan_categories,
        'current_sorting': current_sorting,
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
            messages.error(request, 'Failed to add plan. Please ensure the form is valid.')
    else:
        form = PlanForm()

    template = 'plans/add_plan.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

@login_required
def edit_plan(request, plan_id):
    """ Edit a plan """
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only admin has access to this')
        return redirect(reverse('home'))

    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        form = PlanForm(request.POST, request.FILES, instance=plan)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated plan')
            return redirect(reverse('plan_detail', args=[plan.id]))
        else:
            messages.error(request, 'Failed to update plan. Please ensure the form is valid.')
    else:
        form = PlanForm(instance=plan)
        messages.info(request, f'You are editing {plan.name}')

    template = 'plans/edit_plan.html'
    context = {
        'form': form,
        'plan': plan,
    }

    return render(request, template, context)


@login_required
def delete_plan(request, plan_id):
    """ Delete a plan with validation """
    if not request.user.is_superuser:
        messages.error(request, 'sorry, only admin has access to this')
        return redirect(reverse('home'))

    plan = get_object_or_404(Plan, pk=plan_id)
    if request.method == 'POST':
        plan.delete()
        messages.success(request, 'Successfully deleted plan')
        return redirect('plans')

    template = 'plans/delete_plan_form.html'
    context = {
        'plan': plan,
    }

    return render(request, template, context)
