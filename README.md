# ОПИСАНИЕ РАБОТЫ API

### Предоставление студенту доступа к продукту.

Считается, что у пользователя есть доступ к продукту, если он добавлен в одну из групп, привязанных к продукту.
Предоставить доступ можно отправив get-запрос на url **/give_access/<product_id>/<user_id>/**, где <product_id> - id продукта к которому следует предоставить доступ, a <user_id> - id пользователя которому следует предоставить доступ.
В ответе придет информация о предоставлении пользователю доступа к продукту.

Пример ответа:
```json
"Курс уже начался. Мест в группах нет."
```

### Информация о продуктах.

Получить Информацию о продуктах можно получить отправив get-запрос на url **/products_info**.

Пример ответа:
```json
[
    {
        "id": 1,
        "lessons_quantity": 4,
        "product_name": "python developer curs",
        "start_date": "2024-02-29T17:52:46Z",
        "max_students_in_group": 10,
        "min_students_in_group": 0,
        "price": 5000,
        "creator": 1
    },
    {
        "id": 2,
        "lessons_quantity": 3,
        "product_name": "java developer curs",
        "start_date": "2024-03-01T18:37:33Z",
        "max_students_in_group": 2,
        "min_students_in_group": 0,
        "price": 5000,
        "creator": 1
    },
    {
        "id": 3,
        "lessons_quantity": 2,
        "product_name": "js developer curs",
        "start_date": "2024-03-01T18:47:19Z",
        "max_students_in_group": 5,
        "min_students_in_group": 0,
        "price": 5000,
        "creator": 1
    }
]
```

### Статистика продуктов.

Получить статистику продуктов можно получить отправив get-запрос на url **/get_products_statistics**.

Пример ответа:

```json
[
    {
        "students_qty": 20,
        "group_occupancy": "100%",
        "percent_of_purchase": "100%"
    },
    {
        "students_qty": 0,
        "group_occupancy": "0%",
        "percent_of_purchase": "0%"
    },
    {
        "students_qty": 0,
        "group_occupancy": "0%",
        "percent_of_purchase": "0%"
    }
]
```

###  Получение списка уроков.

Получить список уроков, относящихся к product, к которому пользователь имеет доступ, можно отправив get-запрос на **/get_student_lessons_list/<product_id>/<user_id>/**, 
где <product_id> - id продукта уроки которого стоит получить, a <user_id> - id пользователя который имеет доступ к этому продукту.

Пример ответа:

```json
[
    {
        "id": 1,
        "lesson_name": "python lesson 1",
        "video_url": "https://www.youtube.com/watch?v=tW7Bg5zMyKI&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=5",
        "product": 1
    },
    {
        "id": 2,
        "lesson_name": "python lesson 2",
        "video_url": "https://www.youtube.com/watch?v=tW7Bg5zMyKI&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=5",
        "product": 1
    },
    {
        "id": 3,
        "lesson_name": "python lesson 3",
        "video_url": "https://www.youtube.com/watch?v=tW7Bg5zMyKI&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=5",
        "product": 1
    },
    {
        "id": 4,
        "lesson_name": "python lesson 4",
        "video_url": "https://www.youtube.com/watch?v=tW7Bg5zMyKI&list=PLA0M1Bcd0w8xZA3Kl1fYmOH_MfLpiYMRs&index=5",
        "product": 1
    }
]
```
