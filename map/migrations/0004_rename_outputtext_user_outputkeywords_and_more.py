# Generated by Django 4.1.2 on 2022-11-01 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("map", "0003_alter_user_inputaudiopath"),
    ]

    operations = [
        migrations.RenameField(
            model_name="user", old_name="outputText", new_name="outputKeywords",
        ),
        migrations.AddField(
            model_name="user", name="outputLinks", field=models.TextField(default=""),
        ),
        migrations.AddField(
            model_name="user", name="outputSummary", field=models.TextField(default=""),
        ),
    ]
