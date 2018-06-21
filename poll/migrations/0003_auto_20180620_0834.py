# Generated by Django 2.0.5 on 2018-06-20 08:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ltiprovider', '0001_initial'),
        ('poll', '0002_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='user',
        ),
        migrations.AddField(
            model_name='response',
            name='lti_user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ltiprovider.LtiUser'),
            preserve_default=False,
        ),
    ]