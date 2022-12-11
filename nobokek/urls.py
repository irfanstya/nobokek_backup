from django.urls import path

from nobokek.views import show_nobokek, show_guest, show_json, show_problem, login_user, logout_user, register, create_problem
from statistic.views import show_statistic


app_name = 'nobokek'

urlpatterns = [
    path('', show_nobokek, name='show_nobokek'),
    path('register/', register, name='register'), #sesuaikan dengan nama fungsi yang dibuat
    path('login/', login_user, name='login'), #sesuaikan dengan nama fungsi yang dibuat
    path('logout/', logout_user, name='logout'), #sesuaikan dengan nama fungsi yang dibuat
    path('guest/', show_guest, name='show_guest'), #sesuaikan dengan nama fungsi yang dibuat
    path('json/', show_json, name='show_json'), #sesuaikan dengan nama fungsi yang dibuat
    path('create_problem/', create_problem, name="create_problem"),
    path('statistic/', show_statistic, name="statistic"),
]