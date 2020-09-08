from django.urls import path

from . import views

urlpatterns = [
    path('', views.participant_list),
    path('<int:pk>/', views.participant_detail),
]