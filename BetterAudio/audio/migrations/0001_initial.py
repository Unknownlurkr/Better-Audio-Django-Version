# Generated by Django 3.1.3 on 2020-11-07 20:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audioPath', models.CharField(max_length=255)),
                ('creatorName', models.CharField(max_length=65)),
                ('userName', models.CharField(max_length=65)),
                ('userPassword', models.CharField(max_length=65)),
                ('userEmail', models.CharField(max_length=255)),
                ('audioTitle', models.CharField(max_length=255)),
                ('audioDescription', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='AudioFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(max_length=10)),
                ('Upload', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.upload')),
            ],
        ),
    ]
