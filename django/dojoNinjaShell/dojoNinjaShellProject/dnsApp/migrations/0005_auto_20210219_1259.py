# Generated by Django 2.2.4 on 2021-02-19 20:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dnsApp', '0004_auto_20210219_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ninja',
            name='dojo_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ninja', to='dnsApp.Dojo'),
        ),
    ]
