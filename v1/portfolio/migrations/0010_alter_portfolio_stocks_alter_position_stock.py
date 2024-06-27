# Generated by Django 4.2.3 on 2024-06-24 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0006_security_securitydata_delete_stockdata"),
        ("portfolio", "0009_position_delete_portfoliostock_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="portfolio",
            name="stocks",
            field=models.ManyToManyField(
                through="portfolio.Position", to="data.security"
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="stock",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="data.security"
            ),
        ),
    ]