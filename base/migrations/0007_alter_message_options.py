# Generated by Django 3.2.21 on 2023-10-02 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_message_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['updated', 'created']},
        ),
    ]
