# Generated by Django 5.0.1 on 2024-01-18 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='exam_result',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
