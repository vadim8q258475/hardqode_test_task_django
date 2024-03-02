from .models import *


def redistribute_groups(product):
    all_students_list = []
    groups = Group.objects.filter(product=product)
    for group in groups:
        for student in group.students.all():
            all_students_list.append(student)
        group.students.clear()
    qty_students_in_group = len(all_students_list)//len(groups)
    list_position = -1
    for group in groups:
        for i in range(qty_students_in_group):
            list_position += 1
            elem = all_students_list[list_position]
            group.students.add(elem)
        group.save()

    distributed_students = qty_students_in_group * len(groups)
    remaining_students = len(all_students_list) - distributed_students
    if remaining_students > 0:
        group_number = -1
        for i in range(distributed_students, len(all_students_list)):
            group_number += 1
            elem = all_students_list[i]
            groups[group_number].students.add(elem)
            groups[group_number].save()




