# Generated by Django 4.1.7 on 2023-03-23 13:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Access',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode', models.IntegerField(default=1, verbose_name='access mode')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chat.chat', verbose_name='chat')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'access',
                'verbose_name_plural': 'accesses',
            },
        ),
    ]
