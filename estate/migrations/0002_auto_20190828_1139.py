# Generated by Django 2.2.4 on 2019-08-28 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]