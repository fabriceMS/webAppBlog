# Generated by Django 3.0.7 on 2020-06-15 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='moderation_text',
            new_name='created_at',
        ),
    ]
