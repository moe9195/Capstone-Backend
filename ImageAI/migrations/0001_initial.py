# Generated by Django 3.0.5 on 2020-04-26 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Method',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ImageAI',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('processed_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('method', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='method', to='ImageAI.Method')),
            ],
        ),
    ]
