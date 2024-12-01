from django.urls import path
from django.contrib import admin
from score import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('salvar_score/', views.salvar_score),
    path('ranking/', views.ranking),
]