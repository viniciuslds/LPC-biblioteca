# Generated by Django 2.2.5 on 2019-09-20 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_biblioteca', '0002_auto_20190920_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emprestimo',
            name='livro',
        ),
        migrations.AddField(
            model_name='emprestimo',
            name='livro',
            field=models.ManyToManyField(blank=True, null=True, to='app_biblioteca.Livro'),
        ),
    ]