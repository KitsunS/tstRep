# Generated by Django 3.1.7 on 2021-04-11 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210411_1538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='section',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='articles.section'),
        ),
    ]
