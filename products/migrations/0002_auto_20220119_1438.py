# Generated by Django 3.2 on 2022-01-19 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        # migrations.RemoveField(
        #     model_name='product',
        #     name='image_url',
        # ),
        # migrations.RemoveField(
        #     model_name='product',
        #     name='sku',
        # ),
        # migrations.AddField(
        #     model_name='product',
        #     name='has_sizes',
        #     field=models.BooleanField(blank=True, default=False, null=True),
        # ),
    ]
