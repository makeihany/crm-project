# Generated by Django 3.0.8 on 2020-07-14 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200714_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.SmallIntegerField(choices=[(1, 'Indoor'), (2, 'Out Door')], default=1, null=True),
        ),
    ]