# Generated by Django 4.0.4 on 2022-06-13 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_order_customer_order_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='tag',
            field=models.ManyToManyField(to='accounts.tag'),
        ),
    ]
