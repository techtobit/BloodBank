# Generated by Django 4.2.13 on 2024-07-02 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('donator', '0003_alter_donator_blood_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonatorDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blood_group', models.CharField(choices=[('A', 'A+ (Positive)'), ('A-', 'A- (Negitive)'), ('B+', 'B+ (Positive)'), ('B-', 'B- (Negitive)'), ('AB+', 'AB+ (Negitive)'), ('O+', 'O+ (Positive)'), ('O-', 'O- (Negitive)')], max_length=15)),
                ('phone_number', models.IntegerField(unique=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='donator_account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Donator',
        ),
    ]