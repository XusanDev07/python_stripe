from django.urls import path
from . import views

app_name = 'items'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('buy/<int:item_id>/', views.create_checkout_session, name='create_checkout_session'),

    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('cancel/', views.cancel_view, name='cancel'),
    path('success/', views.success_view, name='success'),

]
