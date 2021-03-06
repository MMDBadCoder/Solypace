# Generated by Django 3.0.5 on 2020-04-11 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instanceManager', '0002_instance_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='description',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='instance',
            name='label',
            field=models.CharField(default='No label yet', max_length=100),
        ),
        migrations.AlterField(
            model_name='instance',
            name='parent',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='instanceManager.Instance'),
        ),
    ]
