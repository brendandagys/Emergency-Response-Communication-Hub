# Generated by Django 2.2.2 on 2019-07-06 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20190706_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Time of latest message'),
        ),
    ]
