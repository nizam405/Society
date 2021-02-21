# Generated by Django 3.1.6 on 2021-02-21 03:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Subscriber', '0002_auto_20210221_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionFee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('year', models.DateField(default=django.utils.timezone.now)),
                ('mosque', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('graveyeard', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('eidgah', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('mustichal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('tarabih', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Subscriber.subscriber')),
            ],
        ),
        migrations.CreateModel(
            name='Revenue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=2021)),
                ('revenue_type', models.CharField(choices=[('Donation', 'Donation'), ('Others', 'Others')], max_length=10)),
                ('description', models.TextField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('subscriber', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Subscriber.subscriber')),
            ],
        ),
    ]
