# Generated by Django 4.1.3 on 2022-11-30 17:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_books_rented_alter_barrow_borrowdate_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='auther',
            new_name='authur',
        ),
        migrations.AlterField(
            model_name='barrow',
            name='borrowDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 20, 47, 47, 52343)),
        ),
        migrations.AlterField(
            model_name='books',
            name='archiveDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 20, 47, 47, 51833)),
        ),
        migrations.AlterField(
            model_name='user',
            name='joinDate',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 30, 20, 47, 47, 49239)),
        ),
    ]
