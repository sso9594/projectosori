# Generated by Django 3.2.13 on 2022-06-04 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('osoriapp', '0003_freecomment_freepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='freecomment',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='osoriapp.freepost'),
        ),
    ]
