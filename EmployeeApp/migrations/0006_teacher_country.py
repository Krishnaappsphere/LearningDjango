# Generated by Django 4.2 on 2023-04-28 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0005_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
