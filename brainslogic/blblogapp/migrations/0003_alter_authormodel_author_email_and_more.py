# Generated by Django 4.2.5 on 2023-10-03 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blblogapp', '0002_alter_categorymodel_catg_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authormodel',
            name='author_email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='author_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='categorymodel',
            name='updated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
