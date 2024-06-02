# Generated by Django 5.0.6 on 2024-06-02 21:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GovernmentID",
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
                ("title", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Telecommunications",
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
                ("full_legal_name", models.CharField(max_length=300)),
                ("last_name", models.CharField(max_length=150)),
                ("first_name", models.CharField(max_length=150)),
                (
                    "middle_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("government_identification", models.CharField(max_length=150)),
                ("government_identification_number", models.CharField(max_length=150)),
                ("date_of_birth", models.DateField()),
                ("phone_number", models.CharField(max_length=150)),
                ("email_address", models.EmailField(max_length=254)),
                ("street_address", models.CharField(max_length=150)),
                ("city", models.CharField(max_length=150)),
                ("state", models.CharField(max_length=150)),
                ("zip_code", models.CharField(max_length=150)),
                ("country", models.CharField(max_length=150)),
                (
                    "government_identification_photo",
                    models.ImageField(
                        upload_to="portal/images/government_identification_photo"
                    ),
                ),
                ("document_1", models.FileField(upload_to="portal/images/document_1")),
                ("document_2", models.FileField(upload_to="portal/images/document_2")),
                ("document_3", models.FileField(upload_to="portal/images/document_3")),
                (
                    "electronic_signature_full_legal_name",
                    models.CharField(max_length=300),
                ),
                (
                    "government_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="portal.governmentid",
                    ),
                ),
            ],
        ),
    ]