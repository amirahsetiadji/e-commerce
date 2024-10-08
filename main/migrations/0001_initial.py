# Generated by Django 5.1.1 on 2024-09-10 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('stock', models.IntegerField()),
                ('category', models.CharField(max_length=50)),
                ('ingredients', models.TextField()),
                ('allergen_warning', models.TextField()),
                ('customizable', models.BooleanField(default=False)),
                ('date_added', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
