# Generated by Django 3.2.6 on 2021-08-27 06:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210826_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryrelations',
            name='category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.category'),
        ),
        migrations.AddField(
            model_name='categoryrelations',
            name='parent',
            field=models.SmallIntegerField(null=True),
        ),
    ]
