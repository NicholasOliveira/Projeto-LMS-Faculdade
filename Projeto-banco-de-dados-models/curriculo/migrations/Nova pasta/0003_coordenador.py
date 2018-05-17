# Generated by Django 2.0.2 on 2018-05-02 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculo', '0002_disciplina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coordenador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=45, verbose_name='Login')),
                ('senha', models.CharField(max_length=30, verbose_name='Senha')),
                ('nome', models.CharField(max_length=120, verbose_name='Nome')),
                ('email', models.CharField(max_length=80, verbose_name='Email')),
                ('celular', models.CharField(max_length=11, verbose_name='Celular')),
                ('DtExpiração', models.DateField(default='01/01/1900', verbose_name='DtExpiração')),
            ],
        ),
    ]