# Generated by Django 4.2.4 on 2023-08-05 17:22

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_created=True, auto_now=True)),
                ('pseudo_name', models.CharField(max_length=15)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('post_id', models.UUIDField(verbose_name=uuid.uuid4)),
            ],
        ),
    ]
