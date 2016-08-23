# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-08-23 22:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webpage', '0001_initial'),
        ('Fabricante', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='amostra',
            name='analise',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Fabricante.AnaliseSensorial'),
        ),
        migrations.AddField(
            model_name='amostra',
            name='teste',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Fabricante.Teste'),
        ),
        migrations.AddField(
            model_name='analisesensorial',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='teste',
            name='provador',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='webpage.Provador'),
        ),
        migrations.CreateModel(
            name='PerguntaDissertativa',
            fields=[
                ('pergunta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fabricante.Pergunta')),
                ('descricao', models.TextField()),
            ],
            bases=('Fabricante.pergunta',),
        ),
        migrations.CreateModel(
            name='PerguntaHedonica',
            fields=[
                ('pergunta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fabricante.Pergunta')),
                ('hedonica', models.IntegerField(choices=[(1, 'Desgostei Muitissimo'), (2, 'Desgostei Moderadamente'), (3, 'Gostei'), (4, 'Gostei Moderadamente'), (5, 'Gostei Muitissimo')], default=1)),
            ],
            bases=('Fabricante.pergunta',),
        ),
        migrations.CreateModel(
            name='PerguntaSimNao',
            fields=[
                ('pergunta_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fabricante.Pergunta')),
                ('nao', models.BooleanField(default=False, verbose_name='Não')),
                ('sim', models.BooleanField(default=False, verbose_name='Sim')),
            ],
            bases=('Fabricante.pergunta',),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='analise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fabricante.AnaliseSensorial'),
        ),
    ]
