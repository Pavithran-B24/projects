from django.urls import path
from .import views

urlpatterns=[
    path('',views.employee_form,name='employee_create'),
    path('list/',views.employee_list,name = 'employee_read'),
    path('<int:id>/',views.employee_form,name='employee_update'),
    path('delete/<int:id>/',views.employee_delete,name='employee_delete')
]