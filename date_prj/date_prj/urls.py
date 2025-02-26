"""
URL configuration for date_prj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
# from date_app.views import cdt
from date_app.views import dynamicdate

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('date/',cdt),
#     path('', include('date_app.urls')),  # Includes URLs from FSD_app
# ]


# urlpatterns = [
#     path('admin/', admin.site.urls),
  
#     # path('dynamic/<str:s>',dynamicdate), 
#     path('dynamicdate/', dynamicdate, name='dynamicdate'),  # Includes URLs from FSD_app
# ]


from django.contrib import admin
from django.urls import path, include
from date_app.views import dynamicdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dynamic/<str:s>/',dynamicdate),
    path('', include('date_app.urls')),  # Includes URLs from FSD_app
]