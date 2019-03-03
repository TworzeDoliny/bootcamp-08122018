from django.urls import path

from mathematics.views import do_math

urlpatterns = [
    path('<operation>/<int:arg1>/<int:arg2>', do_math)
]
