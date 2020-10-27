# Generated by Django 2.0.2 on 2020-10-27 03:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0003_auto_20201025_0025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dorms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Roomstyle', models.CharField(max_length=50)),
                ('Bathrooms', models.CharField(max_length=50)),
                ('Price', models.IntegerField()),
                ('Safety', models.IntegerField()),
                ('Address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.Amenities')),
            ],
        ),
    ]
