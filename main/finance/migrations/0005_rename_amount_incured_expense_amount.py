# Generated by Django 4.2.8 on 2024-03-14 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0004_alter_savings_amount_saved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='amount_incured',
            new_name='amount',
        ),
    ]
