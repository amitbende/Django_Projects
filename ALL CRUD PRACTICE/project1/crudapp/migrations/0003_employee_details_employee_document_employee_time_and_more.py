# Generated by Django 4.0.4 on 2022-06-12 11:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0002_employee_c_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='details',
            field=models.TextField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='document',
            field=models.FileField(default=django.utils.timezone.now, upload_to='files'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.ImageField(upload_to='photos'),
        ),
    ]
