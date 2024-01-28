# Generated by Django 4.2.9 on 2024-01-24 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.course'),
        ),
        migrations.AlterField(
            model_name='order',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.department'),
        ),
    ]