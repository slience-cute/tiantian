# Generated by Django 2.2.5 on 2019-10-01 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('upwd', models.CharField(max_length=40)),
                ('ushou', models.CharField(max_length=50)),
                ('uyoubian', models.CharField(max_length=6)),
                ('uphone', models.CharField(max_length=11)),
                ('uaddress', models.CharField(max_length=100)),
            ],
        ),
    ]
