# Generated by Django 2.0.2 on 2020-10-28 03:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homes', '0002_auto_20201027_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='amenities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.Amenities'),
        ),
        migrations.AlterField(
            model_name='dorms',
            name='Roomstyle',
            field=models.CharField(choices=[('Single', 'Single'), ('Shared Single', 'Shared Single'), ('Double', 'Double'), ('Triple', 'Triple'), ('Suite', 'Suite'), ('Apartment', 'Apartment')], default='N/A', max_length=50),
        ),
        migrations.AlterField(
            model_name='dorms',
            name='amenities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.Amenities'),
        ),
        migrations.AlterField(
            model_name='house',
            name='amenities',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homes.Amenities'),
        ),
    ]
