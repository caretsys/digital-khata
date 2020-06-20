# Generated by Django 3.0.7 on 2020-06-20 15:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200, null=True)),
                ('gender', models.CharField(max_length=20)),
                ('store_name', models.CharField(max_length=20)),
                ('country', models.CharField(default='Nepal', max_length=20)),
                ('city', models.CharField(default='Kathmandu', max_length=20)),
                ('street', models.CharField(default='Please Update Your Sreet', max_length=50)),
                ('landmark', models.CharField(default='Please Update Your Sreet', max_length=50)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
