from django.shortcuts import render
from .models import Subject

# Create your views here.
def listview(request):
    context={}
    context['dataset']=Subject.objects.all()

    return render(request,'listview.html',context)
