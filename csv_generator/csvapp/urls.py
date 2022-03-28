from django.urls import path, include
from csvapp.models import CsvUser
from rest_framework import routers, serializers, viewsets
from . import views

# api class
class CsvUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CsvUser
        fields = ['first_name', 'middle_name', 'last_name', 'contact', 'email', 'username']

class CsvUserViewSet(viewsets.ModelViewSet):
    queryset = CsvUser.objects.all()
    serializer_class = CsvUserSerializer 

router = routers.DefaultRouter()
router.register(r'users', CsvUserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
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
    path('send-email', views.user_send_mail, name="user.email"),
    path('csv', views.export_to_csv, name="csv"),
    path('login/', views.user_login, name="user.login"),
    path('logout/', views.user_logout, name="user.logout"),
    path('create/', views.user_create, name="user.create"),
    path('show/', views.user_show, name="user.show"),
    path('udpate/', views.user_update, name="user.update"),
    path('profile/', views.user_profile_upload, name="user.profile"),
    # path('edit/<int:id>', views.users_index, name="user.edit"),
   
    # path('delete/<int:id>', views.users_index, name="user.delete"),
]