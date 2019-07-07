# Generated by Django 2.2.2 on 2019-07-06 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='timestamp',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Time of latest message'),
        ),
    ]
