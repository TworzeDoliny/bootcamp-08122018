# Generated by Django 2.1.7 on 2019-03-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='year',
            new_name='production_year',
        ),
        migrations.AddField(
            model_name='car',
            name='body_type',
            field=models.CharField(blank=True, choices=[('sedan', 'sedan'), ('combi', 'combi'), ('hatchback', 'hatchback'), ('cabriolet', 'cabriolet'), ('van', 'van')], max_length=20, null=True),
        ),
    ]
