# Generated by Django 3.0.7 on 2020-06-15 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200615_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='moderation_text',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
