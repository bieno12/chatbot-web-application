# Generated by Django 4.1.7 on 2023-09-06 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='name',
            field=models.CharField(default='Unnamed Conversation', max_length=255),
        ),
    ]
