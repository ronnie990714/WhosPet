# Generated by Django 3.2.8 on 2021-11-19 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='board_name',
            field=models.CharField(default='free', max_length=32, verbose_name='게시판 종류'),
        ),
    ]