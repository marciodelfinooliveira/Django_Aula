# Generated by Django 5.0.3 on 2024-03-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=9)),
                ('uf', models.CharField(max_length=2)),
                ('ddd', models.CharField(max_length=2)),
                ('cidade', models.CharField(max_length=150)),
                ('bairro', models.CharField(max_length=150)),
                ('rua', models.CharField(max_length=255)),
            ],
        ),
    ]