# Generated by Django 4.2.4 on 2023-08-06 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='session_key',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='history',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
