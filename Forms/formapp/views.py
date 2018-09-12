from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .form import NameForm
def get_name(request):
    if request.method=='POST':
        form=NameForm(request.POST)
        if form.is_valid():
            return HttpResponse('Thanks')
    else:
        form=NameForm()
        return render(request,'name.html',{'form':form})
