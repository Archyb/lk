# Generated by Django 4.1.4 on 2022-12-15 07:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Network',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.GenericIPAddressField()),
                ('mask', models.IntegerField()),
                ('isAuth', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField()),
                ('isAuth', models.BooleanField(default=False)),
                ('network', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ips', to='api.network')),
            ],
        ),
    ]
