# Generated by Django 4.2 on 2023-04-16 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('asosiy', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('aktiv', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Ustoz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=50)),
                ('yosh', models.SmallIntegerField()),
                ('jins', models.CharField(choices=[('Ayol', 'Ayol'), ('Erkak', 'Erkak')], max_length=50)),
                ('daraja', models.CharField(choices=[('Bakalavr', 'Bakalavr'), ('Magistr', 'Magistr'), ('Aspirant', 'Aspirant'), ('Doktor', 'Doktor')], max_length=50)),
                ('fan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.fan')),
            ],
        ),
        migrations.AddField(
            model_name='fan',
            name='yonalish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='asosiy.yonalish'),
        ),
    ]