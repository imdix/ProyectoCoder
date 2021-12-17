from django.db import migrations, models



class Migration(migrations.Migration):

    dependencies = [,
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=40)),
                ('numero', models.IntegerField()),
                ('esBueno', models.BooleanField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(max_length=40)),
                ('hinchas', models.IntegerField()),
                ('esGrande', models.BooleanField(null=True)),
            ],
        ),

        migrations.CreateModel(
            name='Estadio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('capacidad', models.IntegerField()),
            ],
        ),

    ]
