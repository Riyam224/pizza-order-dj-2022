from django.urls import path 
from . import views 



urlpatterns = [
    path("", views.index, name="index"),
    path('api/order' , views.order_pizza , name='order_pizza'),
    path('<order_id>/' , views.order , name='order')
]
