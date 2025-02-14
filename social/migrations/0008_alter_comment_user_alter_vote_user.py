# Generated by Django 5.1.5 on 2025-01-19 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0007_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.profile'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social.profile'),
        ),
    ]
