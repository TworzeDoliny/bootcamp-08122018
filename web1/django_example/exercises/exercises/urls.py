"""exercises URL Configuration

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
# from django.contrib import admin
# from django.http import HttpResponse
# from django.urls import path
#
# def hello_world(request):
#     return HttpResponse("Hello World")
#
# def hello_name(request, name):
#     return HttpResponse(f"Hello {name}")
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', hello_world),
#     path('hello/<name>', hello_name)
# ]
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from greetings.views import hello_world, hello_name


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_world),
    path('hello/<name>', hello_name),
    path('maths/', include('mathematics.urls')),
    path('cars/', include('cars.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

