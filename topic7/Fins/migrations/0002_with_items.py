# Generated by Django 3.2.8 on 2021-10-25 12:32

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fins', '0001_without_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('is_sold', models.BooleanField(default=False)),
                ('comments', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_relate', related_query_name='item_filter', to='Fins.department')),
            ],
            options={
                'verbose_name': 'Item',
                'verbose_name_plural': 'Items',
                'ordering': ['id'],
            },
        ),
    ]