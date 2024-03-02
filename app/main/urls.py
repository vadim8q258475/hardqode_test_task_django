from django.urls import path, include
from rest_framework import routers

from .views import *


urlpatterns = [
    path('give_access/<int:product_id>/<int:user_id>/', GiveAccessAPIView.as_view()),
    path('products_info', ProductInfoAPIView.as_view()),
    path('get_student_lessons_list/<int:product_id>/<int:user_id>/', LessonsListAPIView.as_view()),
    path('get_products_statistics', GetStatisticsAPIView.as_view()),
]