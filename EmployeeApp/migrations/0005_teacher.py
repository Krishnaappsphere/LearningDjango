# Generated by Django 4.2 on 2023-04-28 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0004_rename_department_id_employeedepartment_departmentid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('teacherName', models.CharField(max_length=200)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
