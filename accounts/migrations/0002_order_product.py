# Generated by Django 3.0.8 on 2020-07-14 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True, null=True)),
                ('status', models.SmallIntegerField(choices=[('Pending', 1), ('Out For Delivery', 2), ('Delivered', 3)], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.SmallIntegerField(choices=[('Indoor', 1), ('Out Door', 2)], null=True)),
                ('description', models.TextField(max_length=200, null=True)),
            ],
        ),
    ]
