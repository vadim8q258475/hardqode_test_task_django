from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    lessons_quantity = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__'

    def get_lessons_quantity(self, obj):
        length = len(
            Lesson.objects.filter(
                product=Product.objects.get(
                    id=obj.id
                )
            )
        )
        return length


class ProductStatisticsSerializer(serializers.Serializer):

    students_qty = serializers.SerializerMethodField()
    group_occupancy = serializers.SerializerMethodField()
    percent_of_purchase = serializers.SerializerMethodField()

    @staticmethod
    def get_students_qty(obj):
        counter = 0
        for group in Group.objects.filter(product=obj):
            counter += len(group.students.all())
        return counter

    @staticmethod
    def get_group_occupancy(obj):
        percent_list = []
        for group in Group.objects.filter(product=obj):
            value = len(group.students.all()) / obj.max_students_in_group
            percent_list.append(value)
        if len(percent_list) == 0:
            return '0%'
        return f'{int(round(sum(percent_list) / len(percent_list), 2)*100)}%'

    @staticmethod
    def get_percent_of_purchase(obj):
        all_total = 0
        obj_total = 0
        for product in Product.objects.all():
            for group in Group.objects.filter(product=product):
                all_total += len(group.students.all())
                if product == obj:
                    obj_total += len(group.students.all())
        return f'{int(round(obj_total / all_total, 2) * 100)}%'
