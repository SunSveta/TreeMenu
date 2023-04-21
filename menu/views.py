from django.views.generic import ListView

from menu.models import MenuCategories


class MenuCategoriesView(ListView):
    model = MenuCategories
    template_name = 'menu/base.html'


