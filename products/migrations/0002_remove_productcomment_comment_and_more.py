# Generated by Django 4.2 on 2024-05-11 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productcomment',
            name='comment',
        ),
        migrations.RemoveField(
            model_name='productcomment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='productcomment',
            name='deleted_at',
        ),
        migrations.RemoveField(
            model_name='productcomment',
            name='parent_id',
        ),
        migrations.RemoveField(
            model_name='productcomment',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='productcomment',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='productcomment',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='productcomment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]