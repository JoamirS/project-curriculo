# Generated by Django 2.2.2 on 2019-06-08 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dadopessoal',
            old_name='cpf',
            new_name='CPF',
        ),
        migrations.AlterField(
            model_name='dadopessoal',
            name='nascimento',
            field=models.DateField(),
        ),
    ]