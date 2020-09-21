"""askcompany URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# django.conf를 통해 settings를 import해주면 우리에게 필요한
# from django.conf import global_settings
# from askcompany import settings 
# 위 2개를 합쳐서 하나로 import해준다.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('instagram/', include('instagram.urls')),
    
]

if settings.DEBUG: # 개발모드일때는 DEBUG는 True, 서비스에서는 False
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

