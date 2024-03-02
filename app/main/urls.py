from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.SimpleRouter()
router.register(r'products', ProductInfoAPIView)
router.register(r'products_statistics', ProductStatisticsAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('give_access/<int:product_id>/<int:user_id>/', GiveAccessAPIView.as_view()),
    path('get_student_lessons_list/<int:product_id>/<int:user_id>/', LessonsListAPIView.as_view()),
]