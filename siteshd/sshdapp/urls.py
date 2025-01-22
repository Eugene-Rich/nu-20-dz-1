from django.urls import path
from sshdapp import views

app_name = 'sshdapp'

urlpatterns = [
    path('', views.main_view, name='index'),
    path('vvod/', views.vvod_view, name='vvod'),
    path('ftbl/', views.ftbl_view, name='ftbl'),
    path('instrp/', views.instrp_view, name='instrp')

]