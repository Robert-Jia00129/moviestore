from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Petition, PetitionVote
from .forms import PetitionForm

def petition_list(request):
    petitions = Petition.objects.all().order_by("-created_at")
    return render(request, "petitions/list.html", {"petitions": petitions})

def petition_detail(request, pk):
    petition = get_object_or_404(Petition, pk=pk)
    return render(request, "petitions/detail.html", {"petition": petition})

@login_required(login_url='accounts.login')
def petition_create(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)
        if form.is_valid():
            petition = form.save(commit=False)
            petition.created_by = request.user
            petition.save()
            return redirect("petition_list")
    else:
        form = PetitionForm()
    return render(request, "petitions/form.html", {"form": form})

@login_required(login_url='accounts.login')
def petition_vote(request, pk):
    petition = get_object_or_404(Petition, pk=pk)
    PetitionVote.objects.get_or_create(petition=petition, user=request.user, defaults={"vote": True})
    return redirect("petition_detail", pk=pk)