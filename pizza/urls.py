"""Define URL patterns for pizza."""

from django.conf.urls import url

from . import views

urlpatterns = [
    #Home page
    url(r'^$', views.index, name='index'),
    
    #show all available pizzas.
    url(r'^pizza/$', views.pizzas, name='pizza'),
    
    # Details page for each pizza
    url(r'^pizzas/(?P<pizza_id>\d+)/$', views.pizza, name='pizza'),
]