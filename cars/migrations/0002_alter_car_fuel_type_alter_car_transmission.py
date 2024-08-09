# Generated by Django 5.1 on 2024-08-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='fuel_type',
            field=models.CharField(choices=[('бензин', 'бензин'), ('дизель', 'дизель'), ('электричество', 'электричество'), ('гибрид', 'гибрид')], max_length=13),
        ),
        migrations.AlterField(
            model_name='car',
            name='transmission',
            field=models.CharField(choices=[('механическая', 'механическая'), ('автоматическая', 'автоматическая'), ('вариатор', 'вариатор'), ('робот', 'робот')], max_length=14),
        ),
    ]
