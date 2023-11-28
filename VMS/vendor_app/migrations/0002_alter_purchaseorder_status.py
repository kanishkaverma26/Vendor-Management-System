# Generated by Django 4.2.7 on 2023-11-24 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendor_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Complete'), ('Canceled', 'Canceled')], default='Pending', max_length=10),
        ),
    ]
