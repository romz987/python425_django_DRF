# Generated by Django 5.2.1 on 2025-06-04 22:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sections.section', verbose_name='Section')),
            ],
            options={
                'verbose_name': 'Content',
                'verbose_name_plural': 'Content',
                'ordering': ['id'],
            },
        ),
    ]
