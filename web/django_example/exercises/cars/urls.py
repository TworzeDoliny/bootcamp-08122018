from django.urls import path

from cars.views import car_list, car_details

urlpatterns = [
    # /cars
    path('', car_list),
    # /cars/1
    path('<int:id>/', car_details)

]
