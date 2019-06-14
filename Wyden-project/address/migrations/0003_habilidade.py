# Generated by Django 2.2.2 on 2019-06-14 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_auto_20190612_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='habilidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('habilidade1', models.CharField(max_length=50)),
                ('habilidade2', models.CharField(max_length=50)),
                ('habilidade3', models.CharField(max_length=50)),
                ('habilidade4', models.CharField(blank=True, max_length=50, null=True)),
                ('habilidade5', models.CharField(blank=True, max_length=50, null=True)),
                ('habilidade6', models.CharField(blank=True, max_length=50, null=True)),
                ('id_habilidade', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='address.dadoPessoal')),
            ],
        ),
    ]
