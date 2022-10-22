# Generated by Django 4.1.1 on 2022-10-22 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoa', '0003_pessoa_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('tipo', models.CharField(max_length=256)),
                ('vacina', models.BooleanField(default=False)),
                ('descricao', models.CharField(max_length=256)),
            ],
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='ativa',
        ),
        migrations.DeleteModel(
            name='Contato',
        ),
        migrations.AddField(
            model_name='animal',
            name='pessoa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pessoa.pessoa'),
        ),
    ]
