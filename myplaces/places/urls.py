from django.urls import path
from . import views

app_name = 'places'

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.place_list, name='list'),
    path('add/', views.add_place, name='add'),
    path('<int:place_id>/', views.place_detail, name='detail')
]
