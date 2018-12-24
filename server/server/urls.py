"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/activesessions', views.ActiveSessionsViewSet.as_view({'get': 'list'})),
    path('api/session', views.ActiveSessionsViewSet.as_view({'get': 'retrieve'})), #não implementado ainda
    path('api/cpus', views.CPUViewSet.as_view({'get': 'list'})),
    path('api/tablespaces', views.TablespaceViewSet.as_view({'get': 'list'})),
    path('api/tablespaces/<str:tablespace>', views.TablespaceViewSet.as_view({'get': 'retrieve'})), #aqui passa-se o nome do tablespace para se obter toda a info de um tablespace
    path('api/profiles', views.ProfilesViewSet.as_view({'get': 'list'})),
    path('api/roles', views.RolesViewSet.as_view({'get': 'list'})),
    path('api/queries', views.SQLQueryViewSet.as_view({'get': 'list'})),
    path('api/queryhistory', views.SQLQueryViewSet.as_view({'get': 'retrieve'})), #não implementado ainda
    path('api/users', views.UsersViewSet.as_view({'get': 'list'})),
    path('api/user/<str:username>', views.UsersViewSet.as_view({'get': 'retrieve'})), #não implementado ainda
    path('api/pga', views.PGAViewSet.as_view({'get': 'list'})),
    path('api/sga', views.SGAViewSet.as_view({'get': 'list'}))
]
