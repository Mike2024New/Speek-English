# Generated by Django 4.2.16 on 2024-09-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phrase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phrase_en', models.CharField(max_length=300, unique=True, verbose_name='phrase_en')),
                ('phrase_ru', models.CharField(max_length=300, unique=True, verbose_name='phrase_ru')),
            ],
        ),
    ]
