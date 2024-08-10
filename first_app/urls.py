from django.urls import path
from . import views
urlpatterns = [
    path('', views.product),
    path('delete/<int:id>', views.delete_student, name='delete_student')
]
