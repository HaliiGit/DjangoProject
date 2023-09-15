# Generated by Django 4.2.1 on 2023-09-13 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pojisteni_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Udalosti',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cislo_pojistne_smlouvy', models.IntegerField(default=0)),
                ('popis_udalosti', models.CharField(max_length=1000)),
                ('datum_udalosti', models.DateTimeField()),
                ('pojisteni', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pojisteni_app.pojisteni')),
            ],
            options={
                'verbose_name': 'Událost',
                'verbose_name_plural': 'Události',
            },
        ),
    ]
