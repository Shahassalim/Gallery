from django.shortcuts import render
from .forms import Imgform
from .models import ImgModel

# Create your views here.
def Display(request):
    data=ImgModel.objects.all()
    form=Imgform()
    if request.method=='POST':
        form=Imgform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    return render(request,'index.html',{'form':form,'data':data})


