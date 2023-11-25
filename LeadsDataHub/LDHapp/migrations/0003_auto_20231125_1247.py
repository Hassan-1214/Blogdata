# Generated by Django 3.1.14 on 2023-11-25 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LDHapp', '0002_blog_categorie_comment_tag_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leadsform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=20)),
                ('leads_catg', models.CharField(max_length=100)),
                ('catg_name', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('canceled', 'Canceled'), ('pending', 'Pending')], default='pending', max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='blog',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='categorie',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]