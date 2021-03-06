# Generated by Django 3.1.6 on 2021-04-26 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=14)),
                ('slugs', models.CharField(max_length=130)),
                ('timeStamp', models.DateTimeField(blank=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
