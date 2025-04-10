# Generated by Django 5.1.5 on 2025-02-24 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0003_employee_email_address_employee_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task_manager',
            name='task_priority',
            field=models.CharField(choices=[('Medium', 'Medium'), ('High', 'High'), ('Low', 'Low')], max_length=10),
        ),
        migrations.AlterField(
            model_name='task_manager',
            name='task_status',
            field=models.CharField(choices=[('In Progress', 'In Progress'), ('Not Started', 'Not Started'), ('Completed', 'Completed')], max_length=15),
        ),
    ]
