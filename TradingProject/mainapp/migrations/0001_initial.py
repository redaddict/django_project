# Generated by Django 4.2.6 on 2023-10-21 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nifty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BANKNIFTY', models.CharField(max_length=255, verbose_name='BANKNIFTY')),
                ('DATE', models.DateField(verbose_name='DATE')),
                ('TIME', models.TimeField(verbose_name='TIME')),
                ('OPEN', models.FloatField(verbose_name='OPEN')),
                ('HIGH', models.FloatField(verbose_name='HIGH')),
                ('LOW', models.FloatField(verbose_name='LOW')),
                ('CLOSE', models.FloatField(verbose_name='CLOSE')),
                ('VOLUME', models.BigIntegerField(verbose_name='VOLUME')),
            ],
        ),
    ]