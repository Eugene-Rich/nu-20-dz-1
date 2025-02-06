from django.urls import path
from sshdapp import views

app_name = 'sshdapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('vvod/', views.vvod_view, name='vvod'),
    path('ftbl/<str:sez>/', views.TovostListView.as_view(), name='ftbl'),
    path('instrp/<str:uin>/', views.TovostDetail.as_view(), name='instrp'),
    path('spr_sez', views.SezListView.as_view(), name='spr_sez'),
    path('spr_razm', views.RazmListView.as_view(), name='spr_razm')

]