# Generated by Django 5.1.2 on 2024-11-26 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("crops", "0002_auto_20241009_2230"),
    ]

    operations = [
        migrations.AddField(
            model_name="culturas",
            name="loss_percentage",
            field=models.FloatField(
                default=0.0, help_text="Percentual médio de perda no cultivo (%)."
            ),
        ),
        migrations.AddField(
            model_name="culturas",
            name="yield_per_unit",
            field=models.FloatField(
                default=0.0, help_text="Rendimento típico por unidade plantada."
            ),
        ),
        migrations.AddField(
            model_name="culturas",
            name="yield_unit",
            field=models.CharField(
                choices=[
                    ("kg", "Quilogramas"),
                    ("flores", "Flores"),
                    ("maços", "Maços"),
                ],
                default="kg",
                help_text="Unidade de rendimento.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="common_pests",
            field=models.TextField(help_text="Pragas comuns."),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="compatible_plants",
            field=models.TextField(help_text="Plantas compatíveis."),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="crop_type",
            field=models.CharField(
                choices=[
                    ("vegetable", "Vegetal"),
                    ("fruit", "Fruta"),
                    ("grain", "Grão"),
                    ("herb", "Erva"),
                    ("flower", "Flor"),
                ],
                help_text="Tipo de cultura.",
                max_length=20,
            ),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="growing_conditions",
            field=models.TextField(
                help_text="Condições necessárias para o crescimento."
            ),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="harvest_season",
            field=models.CharField(help_text="Estação de colheita.", max_length=100),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="notes",
            field=models.TextField(blank=True, help_text="Notas adicionais."),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="planting_season",
            field=models.CharField(
                help_text="Estação ideal para o plantio.", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="sun_exposure",
            field=models.CharField(
                help_text="Exposição ao sol necessária.", max_length=100
            ),
        ),
        migrations.AlterField(
            model_name="culturas",
            name="watering_needs",
            field=models.CharField(
                help_text="Necessidades de irrigação.", max_length=100
            ),
        ),
    ]