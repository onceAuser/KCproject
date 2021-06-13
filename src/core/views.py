from django.shortcuts import render
from .forms import Tutor_profile_form,create_user_form

# Create your views here.
def profile_view(request):
    if request.method=="POST":
        form=Tutor_profile_form(request.POST)
        if form.is_valid():
            form.save()
            
    form=Tutor_profile_form()    
    template='core/form.html'
    return  render(request,template,{'form':form})


def create_user_view(request):
    if request.method=="POST":
        form=create_user_form(request.POST)
        if form.is_valid():
            form.save()
            
    form=create_user_form()    
    template='core/form.html'
    return  render(request,template,{'form':form})

