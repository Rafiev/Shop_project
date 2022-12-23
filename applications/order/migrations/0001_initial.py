# Generated by Django 4.1.4 on 2022-12-22 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, choices=[('in_processing', 'in_processing'), ('completed', 'completed'), ('declined', 'declined')], max_length=30, null=True)),
                ('is_confirm', models.BooleanField(default=False)),
                ('amount', models.PositiveIntegerField()),
                ('address', models.TextField()),
                ('number', models.CharField(max_length=30)),
                ('total_cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('activation_code', models.UUIDField(default=uuid.uuid4)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='product.product')),
            ],
        ),
    ]
