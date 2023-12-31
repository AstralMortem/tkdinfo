# Generated by Django 4.2.4 on 2023-08-19 19:17

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Belt',
            fields=[
                ('kup', models.CharField(max_length=30)),
                ('kupslug', models.SlugField(default='kup', primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='regulations/belts')),
            ],
        ),
        migrations.CreateModel(
            name='Regulation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('tul', ckeditor.fields.RichTextField()),
                ('kicks', ckeditor.fields.RichTextField()),
                ('self_defence', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('spec_tech', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('power_kicks', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('OFP', ckeditor.fields.RichTextField()),
                ('belt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='regulations.belt')),
            ],
        ),
    ]
