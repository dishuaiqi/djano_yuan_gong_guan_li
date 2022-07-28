# Generated by Django 4.0.6 on 2022-07-24 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_alter_staff_depart_alter_staff_work_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preetyphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telephone', models.CharField(max_length=32, verbose_name='手机号')),
                ('price', models.IntegerField(default=888, verbose_name='价格')),
                ('level', models.SmallIntegerField(choices=[('1', '1级'), ('2', '2级'), ('3', '3级'), ('4', '4级')], default=1, verbose_name='级别')),
                ('status', models.SmallIntegerField(choices=[('1', '未占用'), ('2', '已占用')], default=1, verbose_name='状态')),
            ],
        ),
    ]