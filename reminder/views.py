from django.shortcuts import render, redirect, get_object_or_404
from .models import Policy
from .forms import PolicyForm
from django.contrib.auth.decorators import login_required

@login_required
def policy_list(request):
    policies = Policy.objects.filter(user=request.user)
    return render(request, "reminders/policy_list.html", {"policies": policies})

@login_required
def add_policy(request):
    if request.method == "POST":
        form = PolicyForm(request.POST)
        if form.is_valid():
            policy = form.save(commit=False)
            policy.user = request.user
            policy.save()
            return redirect("policy_list")
    else:
        form = PolicyForm()
    return render(request, "reminders/policy_form.html", {"form": form})

@login_required
def edit_policy(request, pk):
    policy = get_object_or_404(Policy, pk=pk, user=request.user)
    if request.method == "POST":
        form = PolicyForm(request.POST, instance=policy)
        if form.is_valid():
            form.save()
            return redirect("policy_list")
    else:
        form = PolicyForm(instance=policy)
    return render(request, "reminders/policy_form.html", {"form": form})

@login_required
def delete_policy(request, pk):
    policy = get_object_or_404(Policy, pk=pk, user=request.user)
    policy.delete()
    return redirect("policy_list")
