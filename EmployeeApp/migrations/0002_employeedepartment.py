# Generated by Django 4.2 on 2023-04-27 08:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeDepartment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.departments')),
                ('Employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EmployeeApp.employee')),
            ],
        ),
    ]
