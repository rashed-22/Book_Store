# Generated by Django 4.2.3 on 2023-08-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookstoremodel',
            name='last_pub',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
