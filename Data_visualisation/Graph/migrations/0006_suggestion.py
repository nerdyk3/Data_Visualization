# Generated by Django 2.2 on 2019-04-22 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Graph', '0005_csvimport_graph_axis_graphtype'),
    ]

    operations = [
        migrations.CreateModel(
            name='suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('suggestion', models.TextField()),
            ],
        ),
    ]
