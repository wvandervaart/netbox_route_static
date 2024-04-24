# Generated by Django 4.0.3 on 2022-04-01 18:02

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import ipam.fields
import netbox_route_static.fields.ip
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ipam', '0057_created_datetimefield'),
        ('extras', '0072_created_datetimefield'),
        ('dcim', '0153_created_datetimefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaticRoute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('prefix', ipam.fields.IPNetworkField()),
                ('next_hop', netbox_route_static.fields.ip.IPAddressField()),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('metric', models.PositiveSmallIntegerField()),
                ('permanent', models.BooleanField()),
                ('devices', models.ManyToManyField(related_name='static_routes', to='dcim.device')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('vrf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='staticroutes', to='ipam.vrf')),
            ],
        ),
        migrations.AddConstraint(
            model_name='staticroute',
            constraint=models.CheckConstraint(check=models.Q(models.Q(('metric__lte', 255), ('metric__gte', 0))), name='metric_gte_lte'),
        ),
    ]