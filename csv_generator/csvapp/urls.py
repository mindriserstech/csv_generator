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
    path('', views.user_index, name="user.index"),
    path('login/', views.user_login, name="user.login"),
    path('logout/', views.user_logout, name="user.logout"),
    path('create/', views.user_create, name="user.create"),
    path('show/', views.user_show, name="user.show"),
    path('udpate/', views.user_update, name="user.update"),
    # path('store/', views.users_index, name="user.store"),
    # path('edit/<int:id>', views.users_index, name="user.edit"),
   
    # path('delete/<int:id>', views.users_index, name="user.delete"),
]