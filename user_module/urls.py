from django.urls import path
from .views import ItemView, ItemViewUpdate

urlpatterns = [
    path('item-data-api', ItemView.as_view(), name='app-item-api'),
    path('item-data-update-api', ItemViewUpdate.as_view(), name='app-item-update-api'),
]
