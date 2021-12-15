

from django.urls import path
from . import views


urlpatterns = [
    
    path('',views.indexPage,name='homePage'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('solution/<int:pk>/',views.solutionDetail,name='solutionDetail')
]