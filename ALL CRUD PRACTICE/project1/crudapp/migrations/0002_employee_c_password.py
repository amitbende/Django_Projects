# Generated by Django 4.0.4 on 2022-06-07 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='c_password',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
    ]
