from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from .models import Sezon, Razm, Tovost
from .forms import SezonForm

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

    print(f_sez)
    print(f_razm)

    lstsh = {}

    if f_sez is None and f_razm is None:
        c_sez = Sezon.objects.filter(name=f_sez).first()
        c_razm = Razm.objects.filter(name=f_razm).first()

        print(f_sez, c_sez, f_razm, c_razm)

        lstsh = Tovost.objects.filter(razmer=c_razm, sezonnost=c_sez)
        for ish in lstsh:
            print(ish.name)

    else:

        lstsh = Tovost.objects.all()


    return render(request, 'sshdapp/ftbl.html', context={'lstsh' : lstsh})

def instrp_view(request):

    f_uin = request.POST.get("f_uin", "")
    print('*')
    print(f_uin)


    return render(request, 'sshdapp/instrp.html', context={})



#def spr_sez_view(request):
#
#    if request.method == 'GET':
#        form = SezonForm()
#        return render(request, 'sshdapp/spr_sez.html', context={'form': form})
#    else:
#        form = SezonForm(request.POST, files=request.FILES)
#        if form.is_valid():
#            form.save()
#            return HttpResponseRedirect(reverse('blog:index'))
#        else:
#            return render(request, 'blogapp/create.html', context={'form': form})

# CRUD CREATE, READ (LIST, DETAIL), UPDATE, DELETE

class NameContextMixin(ContextMixin):

    def get_context_data(self, *args, **kwargs):
        """
        Отвечает за передачу параметров в контекст
        :param args:
        :param kwargs:
        :return:
        """
        context = super().get_context_data(*args, **kwargs)
        context['name'] = 'Теги'

        #print(context)

        return context

class SezListView(ListView, NameContextMixin):
    model = Sezon
    template_name = 'sshdapp/spr_sez.html'
    context_object_name = 'name'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        print('***')
        zn = Sezon.objects.all()
        print(len(zn))

        return zn

class RazmListView(ListView, NameContextMixin):
    model = Razm
    template_name = 'sshdapp/spr_razm.html'
    context_object_name = 'name'

    def get_queryset(self):
        """
        Получение данных
        :return:
        """
        print('***')
        zn = Razm.objects.all()
        print(len(zn))

        return zn

class TovostListView(ListView, NameContextMixin):
    model = Tovost
    template_name = 'sshdapp/ftbl.html'
    context_object_name = 'name'

    def get_queryset(self):

        prm = self.kwargs.get('sez')
        print(type(prm))
        print(prm)
        ls = prm.split('&')
        print(ls)

        prmsez = ls[0]
        if len(ls) == 1:
            prmrazm = ' '
        else:
            prmrazm = ls[1]
            prmrazm = prmrazm.replace(' ','/')

        c_sez = Sezon.objects.filter(name=prmsez).first()

        #prmrazm = ' ' #self.kwargs.get('razm')
        print(type(prmrazm))
        print(prmrazm)
        c_razm = Razm.objects.filter(name=prmrazm).first()

        if prmsez == ' ':
            zn = Tovost.objects.all()
        else:
            if prmrazm == ' ':
                zn = Tovost.objects.filter(sezonnost=c_sez).all()
            else:
                zn = Tovost.objects.filter(razmer=c_razm, sezonnost=c_sez).all()

        return zn

class TovostDetail(DetailView, NameContextMixin):
    model = Tovost
    template_name = 'sshdapp/instrp.html'

    def get(self, request, *args, **kwargs):

        self.uin = kwargs['uin']
        return super().get(request, *args, **kwargs)
    def get_object(self, queryset=None):

        return get_object_or_404(Tovost, uin=self.uin)