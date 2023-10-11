from django.urls import path
from . import views


urlpatterns = [
    # add more URL patterns here
    path('menu/',views.MenuItems.as_view()),
    path('menu/<int:pk>', views.SingleMenuItem.as_view()),

]