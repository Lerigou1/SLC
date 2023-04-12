# Generated by Django 4.1.7 on 2023-04-12 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listas', '0006_produto_rename_nome_lista_nome_lista_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='nome',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='nome', to='listas.lista'),
            preserve_default=False,
        ),
    ]
