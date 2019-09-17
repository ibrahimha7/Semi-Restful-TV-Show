from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_show',views.add_show),
    path('create_show',views.create_show),
    path('show/<int:num>',views.show),
    path('edit_show/<int:num>',views.edit_show),
    path('submit_edit/<int:num>',views.submit_edit),
    path('delete_show/<int:num>',views.delete_show),
]