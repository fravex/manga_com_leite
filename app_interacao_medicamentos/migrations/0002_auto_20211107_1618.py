# Generated by Django 3.2.9 on 2021-11-07 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_interacao_medicamentos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anvisanomeprincipioativo',
            options={'managed': True},
        ),
        migrations.CreateModel(
            name='DrugbankAnvisa',
            fields=[
                ('drugbank', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='app_interacao_medicamentos.drugbanknome')),
                ('matchingvalue', models.FloatField(blank=True, db_column='matchingValue', null=True)),
                ('id_pativo', models.ForeignKey(db_column='id_pAtivo', on_delete=django.db.models.deletion.DO_NOTHING, to='app_interacao_medicamentos.anvisaprincipioativo')),
            ],
            options={
                'db_table': 'drugbank_anvisa',
                'managed': True,
                'unique_together': {('drugbank', 'id_pativo')},
            },
        ),
    ]
