# Generated by Django 3.1.6 on 2022-04-26 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220426_1833'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dato',
            old_name='prefix',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='dato',
            old_name='sufix',
            new_name='country',
        ),
        migrations.AddField(
            model_name='dato',
            name='state',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]