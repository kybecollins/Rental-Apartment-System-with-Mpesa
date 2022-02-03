# Generated by Django 3.2.5 on 2021-09-21 18:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mpesa_api', '0002_auto_20210921_1213'),
    ]

    operations = [
        migrations.AddField(
            model_name='lnmonline',
            name='tenant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='lnmonline',
            name='Amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]