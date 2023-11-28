# Generated by Django 4.2.7 on 2023-11-28 21:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('cat', 'cats'), ('dog', 'dogs')], max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Shelter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('year_of_foundation', models.DateField()),
                ('mail', models.EmailField(blank=True, max_length=70, unique=True)),
                ('phone', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=50)),
                ('link', models.URLField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=15)),
                ('breed', models.CharField(max_length=15)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='animals/')),
                ('info', models.TextField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.category')),
                ('shelter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.shelter')),
            ],
        ),
    ]