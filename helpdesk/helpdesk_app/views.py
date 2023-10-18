from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import ProblemForm
from .models import Problem
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import get_object_or_404


def index(request):
    if request.user.is_authenticated:
        return redirect('problem-list')
    else:
        return render(request, 'helpdesk_app/index.html')


def create_problem(request):
    if request.method == 'POST':
        form = ProblemForm(request.POST)
        if form.is_valid():
            problem = form.save(commit=False)
            assigned_user = form.cleaned_data['assigned_user']
            problem.assigned_user = assigned_user
            problem.save()
            return redirect('index')
    else:
        form = ProblemForm()
    return render(request, 'helpdesk_app/create_problem.html', {'form': form})


def problem_list(request):
    user = request.user
    if user.is_authenticated:
        if user.groups.filter(name='Reception').exists():
            problems = Problem.objects.filter(assigned_user=user)
        else:
            problems = Problem.objects.filter(assigned_user=user)
        return render(request, 'helpdesk_app/problem_list.html', {'problems': problems})
    else:
        return redirect('index')


def problem_detail(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    users = User.objects.all()
    if request.method == 'POST':
        assigned_user_id = request.POST.get('assigned_user')
        if assigned_user_id:
            new_assigned_user = get_object_or_404(User, id=assigned_user_id)
            problem.assigned_user = new_assigned_user
        problem.actions = request.POST.get('actions', '')
        new_status = request.POST.get('status', 'new')
        problem.status = new_status
        problem.save()
        return HttpResponseRedirect(reverse('problem-list'))
    return render(request, 'helpdesk_app/problem_detail.html', {'problem': problem, 'users': users})


