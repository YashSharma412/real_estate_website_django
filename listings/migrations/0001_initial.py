# Generated by Django 5.0.6 on 2024-05-24 11:34

import datetime
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=400)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(5)])),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=3)),
                ('garage', models.IntegerField(blank=True, default=0, null=True)),
                ('sqr_ft', models.IntegerField()),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=6)),
                ('img_main', models.ImageField(upload_to='photos/homes/%Y/%m/%d/')),
                ('img_1', models.ImageField(blank=True, upload_to='photos/homes/%Y/%m/%d/')),
                ('img_2', models.ImageField(blank=True, upload_to='photos/homes/%Y/%m/%d/')),
                ('img_3', models.ImageField(blank=True, upload_to='photos/homes/%Y/%m/%d/')),
                ('img_4', models.ImageField(blank=True, upload_to='photos/homes/%Y/%m/%d/')),
                ('img_5', models.ImageField(blank=True, upload_to='photos/homes/%Y/%m/%d/')),
                ('img_6', models.ImageField(blank=True, upload_to='photos/homes/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateField(blank=True, default=datetime.datetime.now)),
                ('list_date_created_at', models.DateField(auto_now_add=True)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
