from django.shortcuts import render
from .models import Sezon, Razm, Tovost

# Create your views here.
def main_view(request):
    pass
    return render(request, 'sshdapp/index.html', context={})

def vvod_view(request):
    pass
    return render(request, 'sshdapp/vvod.html', context={})

def ftbl_view(request):

    f_sez = request.POST.get("f_sez", "")
    f_razm = request.POST.get("f_razm", "")

    c_sez = Sezon.objects.filter(name=f_sez).first()
    c_razm = Razm.objects.filter(name=f_razm).first()

    print(f_sez, c_sez, f_razm, c_razm)

    lstsh = Tovost.objects.filter(razmer=c_razm, sezonnost=c_sez)
    for ish in lstsh:
        print(ish.name)

    return render(request, 'sshdapp/ftbl.html', context={'lstsh' : lstsh})

def instrp_view(request):
    pass
    return render(request, 'sshdapp/instrp.html', context={})
