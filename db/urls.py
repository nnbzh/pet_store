from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_pets, name='pets'),
    # path('pets/<int:todo_id>', views.get_pet, name='pet'),
    # path('pets/<int:todo_id>/delete', views.delete, name='delete_pet'),
    # path('pets/<int:todo_id>/update', views.update, name='update_pet'),
]