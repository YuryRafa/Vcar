# Generated by Django 4.2 on 2023-05-02 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluguel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=30)),
                ('data_nasc', models.DateField(max_length=8)),
                ('endereço', models.CharField(max_length=30)),
            ],
        ),
    ]
