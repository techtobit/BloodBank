# Generated by Django 4.2.13 on 2024-07-01 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donator', '0002_alter_donator_blood_group_alter_donator_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donator',
            name='blood_group',
            field=models.CharField(choices=[('A', 'A+ (Positive)'), ('A-', 'A- (Negitive)'), ('B+', 'B+ (Positive)'), ('B-', 'B- (Negitive)'), ('AB+', 'AB+ (Negitive)'), ('O+', 'O+ (Positive)'), ('O-', 'O- (Negitive)')], max_length=15),
        ),
    ]