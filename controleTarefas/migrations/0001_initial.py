# Generated by Django 4.2.5 on 2023-09-21 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AlunosEntidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='DisciplinasEntidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=70)),
                ('descrição', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TarefasEntidade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=70)),
                ('descrição', models.TextField()),
                ('data', models.DateTimeField()),
                ('completo', models.BooleanField()),
                ('AlunosTarefas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='controleTarefas.alunosentidade')),
                ('DisiplinasTarefas', models.ManyToManyField(to='controleTarefas.disciplinasentidade')),
            ],
        ),
    ]
