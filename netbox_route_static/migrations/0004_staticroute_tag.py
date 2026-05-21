from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('netbox_route_static', '0003_model_ordering_and_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticroute',
            name='tag',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]