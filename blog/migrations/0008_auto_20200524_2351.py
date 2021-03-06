# Generated by Django 3.0.6 on 2020-05-24 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likes',
            name='post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='likes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='blog.Profile'),
        ),
    ]
