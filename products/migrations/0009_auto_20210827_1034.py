# Generated by Django 3.2.6 on 2021-08-27 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_rename_category_id_categoryrelations_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productlocalization',
            name='column_type',
        ),
        migrations.RemoveField(
            model_name='productlocalization',
            name='language',
        ),
        migrations.RemoveField(
            model_name='productlocalization',
            name='product_id',
        ),
        migrations.DeleteModel(
            name='ProductLang',
        ),
        migrations.DeleteModel(
            name='ProductLocalization',
        ),
    ]
