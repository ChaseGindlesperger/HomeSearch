# Generated by Django 3.1.2 on 2020-10-28 00:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.CharField(default='0', max_length=10, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('Laundry', models.CharField(choices=[('None', 'None'), ('Room', 'Room'), ('Building', 'Building')], default='N/A', max_length=50)),
                ('Kitchen', models.CharField(choices=[('None', 'None'), ('Half', 'Half'), ('Full', 'Full')], default='N/A', max_length=50)),
                ('CommonAreas', models.CharField(choices=[('None', 'None'), ('Few', 'Few'), ('Many', 'Many')], default='N/A', max_length=50)),
                ('AC', models.CharField(choices=[('None', 'None'), ('Central', 'Central'), ('Window', 'Window')], default='N/A', max_length=50)),
                ('Furnished', models.BooleanField()),
                ('InternetTV', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.CharField(default='0', max_length=10, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.CharField(default='0', max_length=10, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('Bedrooms', models.IntegerField()),
                ('Bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('Price', models.IntegerField()),
                ('Safety', models.CharField(choices=[('Least Safe', 'Least Safe'), ('Less Safe', 'Less Safe'), ('More Safe', 'More Safe'), ('Most Safe', 'Most Safe')], default='N/A', max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('amenities', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='homes.amenities')),
            ],
        ),
        migrations.CreateModel(
            name='Dorms',
            fields=[
                ('id', models.CharField(default='0', max_length=10, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Roomstyle', models.CharField(choices=[('Single', 'Single'), ('Shared Single', 'Shared Single'), ('Double', 'Double'), ('Triple', 'Triple')], default='N/A', max_length=50)),
                ('Bathrooms', models.CharField(choices=[('Private', 'Private'), ('Communal', 'Communal')], default='N/A', max_length=50)),
                ('Price', models.IntegerField()),
                ('Safety', models.CharField(choices=[('Least Safe', 'Least Safe'), ('Less Safe', 'Less Safe'), ('More Safe', 'More Safe'), ('Most Safe', 'Most Safe')], default='N/A', max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('amenities', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='homes.amenities')),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.CharField(default='0', max_length=10, primary_key=True, serialize=False)),
                ('Address', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('Bedrooms', models.IntegerField()),
                ('Bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('Price', models.IntegerField()),
                ('Safety', models.CharField(choices=[('Least Safe', 'Least Safe'), ('Less Safe', 'Less Safe'), ('More Safe', 'More Safe'), ('Most Safe', 'Most Safe')], default='N/A', max_length=50)),
                ('image', models.ImageField(default='default.jpg', upload_to='images/')),
                ('amenities', models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='homes.amenities')),
            ],
        ),
    ]
