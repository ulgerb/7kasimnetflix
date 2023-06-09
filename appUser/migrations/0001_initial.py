# Generated by Django 4.1.5 on 2023-05-12 17:28

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
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Profil Adı')),
                ('image', models.ImageField(upload_to='profile', verbose_name='Profil Resmi')),
                ('password', models.CharField(default=0, max_length=50, verbose_name='Profil Şifre')),
                ('password_active', models.BooleanField(default=False, verbose_name='Şifre Aktif Et')),
                ('kid', models.BooleanField(default=False, verbose_name='Çocuk Hesabı')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı')),
            ],
        ),
    ]
