from django.urls import path
from .views import *

urlpatterns = [
    path('',employee_list,name='employee_list'),
    path('create/',employee_create,name='employee_create'),
    path('<int:pk>/edit/',employee_update,name='employee_update'),
    path('<int:pk>/delete/',employee_delete,name='employee_delete'),
    
]
