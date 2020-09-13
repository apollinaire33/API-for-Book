# Generated by Django 3.1.1 on 2020-09-12 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='author',
            new_name='author_name',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='email',
            new_name='decription',
        ),
        migrations.RemoveField(
            model_name='article',
            name='date',
        ),
        migrations.AlterField(
            model_name='article',
            name='id',
            field=models.IntegerField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
