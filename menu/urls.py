from django.urls import path

from menu.apps import MenuConfig
from menu.views import MenuCategoriesView

app_name = MenuConfig.name

urlpatterns = [
    path('', MenuCategoriesView.as_view(), name='index'),
]
