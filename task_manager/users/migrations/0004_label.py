# Generated by Django 3.2.8 on 2021-12-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_task'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                    serialize=False,
                    verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='name')),
            ],
        ),
    ]
