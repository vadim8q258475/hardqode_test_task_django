from datetime import datetime

from rest_framework import generics
from django.shortcuts import render
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet
from django.utils import timezone

from .utils import *
from .models import *
from .serializers import *


class ProductInfoAPIView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductStatisticsAPIView(ListModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductStatisticsSerializer


class GiveAccessAPIView(APIView):

    def get(self, request, product_id, user_id):
        try:
            user = User.objects.get(id=user_id)
        except:
            return Response('Введен некорректный id пользователя.')
        try:
            product = Product.objects.get(id=product_id)
        except:
            return Response('Введен некорректный id продукта.')
        product = Product.objects.get(id=product_id)
        group_queryset = Group.objects.filter(product=product)
        for group in group_queryset:
            if user in group.students.all():
                return Response(f'Пользователь {user.username} уже имеет доступ к продукту {product.product_name}.')
            if len(group.students.all()) < product.max_students_in_group:
                group.students.add(user)
                group.save()
                if timezone.now() < product.start_date:
                    redistribute_groups(product)
                return Response(f'Пользователю {user.username} успешно предоставлен доступ к {product.product_name}.')

        if timezone.now() < product.start_date:
            new_group = Group.objects.create(
                product=product,
                group_name=f'group{len(group_queryset) + 1}_{product.product_name}'
            )
            new_group.students.add(user)
            new_group.save()
            redistribute_groups(product)

            return Response(f'Пользователю {user.username} успешно предоставлен доступ к {product.product_name}.')
        return Response('Курс уже начался. Мест в группах нет.')


class LessonsListAPIView(APIView):

    def get(self, request, product_id, user_id):
        try:
            user = User.objects.get(id=user_id)
        except:
            return Response('Введен некорректный id пользователя.')
        try:
            product = Product.objects.get(id=product_id)
        except:
            return Response('Введен некорректный id продукта.')
        group_queryset = Group.objects.filter(product=product)
        for group in group_queryset:
            if user in group.students.all():
                lessons_queryset = Lesson.objects.filter(product=product)
                lessons_data = LessonSerializer(lessons_queryset, many=True).data
                return Response(lessons_data)
        return Response(f'У пользователя {user.username} нет доступа к {product.product_name}.')



