from django.urls import path
from . import views

app_name = 'recipe'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.detail, name='detail'),
    path('create/', views.create, name='create'),
#    path('create_1/',views.create_1,name = 'create_1'),

]
