from django.shortcuts import render


# Create your views here.
def conditions(request):
    d={'A':300,'B':550,'C':1000}
    return render(request,'conditions.html',context=d)
