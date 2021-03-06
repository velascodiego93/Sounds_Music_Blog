# Generated by Django 4.0.3 on 2022-04-24 22:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='Missing title', max_length=50)),
                ('subtitle', models.CharField(default='Missing subtitle', max_length=100)),
                ('date_of_publication', models.DateField(default=django.utils.timezone.now)),
                ('author', models.CharField(default='Missing author', max_length=40)),
                ('post', models.CharField(max_length=2500)),
            ],
        ),
    ]
