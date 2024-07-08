from django.urls import path
from .views import item, update_item, delete_item, IndexClassView, DetailClassView, CreateItem


app_name = 'food'

urlpatterns = [
    path('', IndexClassView.as_view(), name = 'index'),
    path('<int:pk>', DetailClassView.as_view(), name='detail'),
    path('item', item, name='item'),
    path('add', CreateItem.as_view(), name='create_item'),
    path('update/<int:id>/', update_item, name='update_item'),
    path('delete/<int:id>/', delete_item, name='delete_item'),
]