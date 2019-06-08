# Generated by Django 2.2.2 on 2019-06-08 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dadoPessoal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('nacionalidade', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('estadocivil', models.CharField(max_length=20)),
                ('naturalidade', models.CharField(max_length=30)),
                ('uf', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduacao', models.CharField(max_length=50)),
                ('universidadegraduacao', models.CharField(max_length=50)),
                ('cursograduacao', models.CharField(max_length=50)),
                ('anoformacaograduacao', models.CharField(max_length=4)),
                ('posgraduacao', models.CharField(max_length=50)),
                ('universidadeposgraduacao', models.CharField(max_length=50)),
                ('cursopos', models.CharField(max_length=50)),
                ('anoformacaoposgraduacao', models.CharField(max_length=4)),
                ('id_formacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.dadoPessoal')),
            ],
        ),
        migrations.CreateModel(
            name='enderecoUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rua', models.CharField(max_length=50)),
                ('numero', models.IntegerField()),
                ('bairro', models.CharField(max_length=30)),
                ('quadra', models.IntegerField()),
                ('cep', models.IntegerField()),
                ('id_enderecoUsuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.dadoPessoal')),
            ],
        ),
        migrations.CreateModel(
            name='contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255)),
                ('celular1', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=10)),
                ('celular2', models.CharField(max_length=11)),
                ('id_formacao', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.dadoPessoal')),
            ],
        ),
    ]