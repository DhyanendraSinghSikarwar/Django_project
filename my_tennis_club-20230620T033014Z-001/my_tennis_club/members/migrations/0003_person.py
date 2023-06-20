# Generated by Django 4.1.7 on 2023-03-09 07:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_member_joined_date_member_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField(null=True)),
                ('email', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('member_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.member')),
            ],
        ),
    ]
