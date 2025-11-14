from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_view, name='hello'), # function based view
    path('about/', view.AboutView.as-view(). name='about'), # class based view
]