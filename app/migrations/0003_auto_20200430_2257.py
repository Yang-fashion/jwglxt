# Generated by Django 2.2.11 on 2020-04-30 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200430_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_political_status',
            field=models.CharField(choices=[('1', '中共党员'), ('2', '共青团员'), ('3', '群众')], default='群众', max_length=20, null=True, verbose_name='政治面貌'),
        ),
    ]