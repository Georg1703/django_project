# Generated by Django 3.2.6 on 2021-08-26 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20210826_1516'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLocalizationColumns',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='productlocalization',
            name='column_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.productlocalizationcolumns'),
        ),
    ]
