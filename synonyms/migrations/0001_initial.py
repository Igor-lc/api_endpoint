# Generated by Django 4.2.6 on 2023-11-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Synonyms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_synonyms', models.TextField()),
                ('ukr_synonyms', models.TextField()),
            ],
        ),
    ]
