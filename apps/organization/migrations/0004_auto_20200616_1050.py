# Generated by Django 2.2.6 on 2020-06-16 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_auto_20200616_1027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseorg',
            old_name='course_name',
            new_name='course_nums',
        ),
    ]