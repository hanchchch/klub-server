# Generated by Django 3.2.6 on 2021-08-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20210827_1655'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Options',
            new_name='Option',
        ),
        migrations.RemoveField(
            model_name='optionvalue',
            name='quantity',
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('values', models.ManyToManyField(related_name='quantities', to='product.OptionValue')),
            ],
        ),
    ]
