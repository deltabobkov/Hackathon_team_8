# Generated by Django 4.2.6 on 2023-10-25 14:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_name",
                    models.CharField(max_length=25, verbose_name="Фамилия"),
                ),
                (
                    "first_name",
                    models.CharField(max_length=20, verbose_name="Имя"),
                ),
                (
                    "middle_name",
                    models.CharField(max_length=25, verbose_name="Отчество"),
                ),
                (
                    "image",
                    models.ImageField(
                        default=None,
                        null=True,
                        upload_to="candidates/images/",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[
                            ("М", "Мужской"),
                            ("Ж", "Женский"),
                            ("Не выбран", "Не выбран"),
                        ],
                        default="Не выбран",
                        max_length=10,
                        verbose_name="Пол кандидата",
                    ),
                ),
                (
                    "age",
                    models.PositiveIntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(18),
                            django.core.validators.MaxValueValidator(90),
                        ],
                        verbose_name="Возраст",
                    ),
                ),
                (
                    "contacts_phone",
                    models.CharField(max_length=20, verbose_name="Телефон"),
                ),
                (
                    "contacts_email",
                    models.EmailField(
                        max_length=255, unique=True, verbose_name="Почта"
                    ),
                ),
                (
                    "contacts_other",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        verbose_name="Другой контакт",
                    ),
                ),
                (
                    "activity",
                    models.CharField(
                        choices=[
                            ("AC", "Активный"),
                            ("OH", "В ожидании"),
                            ("NA", "Не доступен"),
                        ],
                        default="NA",
                        max_length=2,
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        blank=True,
                        max_length=150,
                        verbose_name="Местонахождение",
                    ),
                ),
                ("about_me", models.TextField(verbose_name="Обо мне")),
            ],
            options={
                "verbose_name": "Кандидат",
                "verbose_name_plural": "Кандидаты",
                "ordering": ["last_name"],
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
            options={
                "verbose_name": "Кандидат для контакта",
                "verbose_name_plural": "Кандидаты для контакта",
            },
        ),
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "spec_id",
                    models.PositiveIntegerField(
                        verbose_name="ID Специальности"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Название курса",
                "verbose_name_plural": "Названия курсов",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Education",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Образование детально",
                    ),
                ),
                (
                    "level",
                    models.CharField(
                        choices=[
                            ("H", "Высшее"),
                            ("M", "Магистр"),
                            ("B", "Бакалавр"),
                            ("UNH", "Неоконченное высшее"),
                            ("PhD", "Кандидат наук"),
                            ("Ph.D", "Доктор наук"),
                            ("Не выбрано", "Не выбрано"),
                        ],
                        default="H",
                        max_length=20,
                        verbose_name="Уровень образования",
                    ),
                ),
                (
                    "date_start",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000),
                            django.core.validators.MaxValueValidator(9999),
                        ],
                        verbose_name="Дата начала учебы",
                    ),
                ),
                (
                    "date_expiration",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000),
                            django.core.validators.MaxValueValidator(9999),
                        ],
                        verbose_name="Дата окончания учебы",
                    ),
                ),
                (
                    "name_university",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Учебное заведение",
                    ),
                ),
                (
                    "faculty",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Факультет"
                    ),
                ),
                (
                    "specialization",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Специализация",
                    ),
                ),
            ],
            options={
                "verbose_name": "Образование",
                "verbose_name_plural": "Образования",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="EmploymentType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=20,
                        unique=True,
                        verbose_name="Тип занятости",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=20,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Тип заянятости",
                "verbose_name_plural": "Типы заянятости",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=20, unique=True, verbose_name="Опыт работы"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=20,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Опыт работы",
                "verbose_name_plural": "Опыт работы",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="ExperienceDetailed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255,
                        unique=True,
                        verbose_name="Опыта работы детальный",
                    ),
                ),
                (
                    "date_start",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000),
                            django.core.validators.MaxValueValidator(9999),
                        ],
                        verbose_name="Дата начала работы",
                    ),
                ),
                (
                    "date_expiration",
                    models.IntegerField(
                        validators=[
                            django.core.validators.MinValueValidator(1000),
                            django.core.validators.MaxValueValidator(9999),
                        ],
                        verbose_name="Дата окончания работы",
                    ),
                ),
                (
                    "post",
                    models.CharField(max_length=255, verbose_name="Должность"),
                ),
                (
                    "responsibilities",
                    models.TextField(
                        verbose_name="Обязанности на рабочем месте"
                    ),
                ),
            ],
            options={
                "verbose_name": "Опыт работы детальный",
                "verbose_name_plural": "Опыт работы детальный",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="HardCands",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=255, verbose_name="Название"),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255, verbose_name="Уникальный слаг"
                    ),
                ),
            ],
            options={
                "verbose_name": "Hard скилл",
                "verbose_name_plural": "Hard скиллы",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Level",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=10, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=10,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Уровень",
                "verbose_name_plural": "Уровни",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Soft",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Soft скилл",
                "verbose_name_plural": "Soft скиллы",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Specialization",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=255, unique=True, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=255,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "Направление специальности",
                "verbose_name_plural": "Направления специальности",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="WorkSchedule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=20,
                        unique=True,
                        verbose_name="График работы",
                    ),
                ),
                (
                    "slug",
                    models.SlugField(
                        max_length=20,
                        unique=True,
                        verbose_name="Уникальный слаг",
                    ),
                ),
            ],
            options={
                "verbose_name": "График работы",
                "verbose_name_plural": "Графики работы",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Track",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "candidate",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="tracks",
                        to="candidates.candidate",
                    ),
                ),
            ],
            options={
                "verbose_name": "Отслеживаемый",
                "verbose_name_plural": "Отслеживаемые",
            },
        ),
    ]
