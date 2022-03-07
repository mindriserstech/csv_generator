from django.urls import path
from . import views
urlpatterns = [
    # this path() method takes three parameter
    # 1. url i.e '/usertypes/'
    # 2. views.<function_name> i.e views.usertype_index
    # 3. name="<unique_route_name>" i.e name="usertype.name"
    path('usertypes/', views.usertype_index, name="usertype.index"),
    path('usertypes/create/', views.usertype_create, name="usertype.create"),
    path('usertypes/store/', views.usertype_store, name="usertype.store"),
    path('usertypes/udpate/', views.usertype_update, name="usertype.udpate"),
    path('usertypes/edit/<int:id>', views.usertype_edit, name="usertype.edit"),
    path('usertypes/show/<int:id>', views.usertype_show, name="usertype.show"),
    path('usertypes/delete/<int:id>', views.usertype_delete, name="usertype.delete"),

    # user
    # path('/users/', views.usertype_index, name="users.index"),
    # path('/users/create/', views.users_index, name="users.create"),
    # path('/users/store/', views.users_index, name="users.store"),
    # path('/users/udpate/', views.users_index, name="users.udpate"),
    # path('/users/edit/<int:id>', views.users_index, name="users.edit"),
    # path('/users/show/<int:id>', views.users_index, name="users.show"),
    # path('/users/delete/<int:id>', views.users_index, name="users.delete"),
]