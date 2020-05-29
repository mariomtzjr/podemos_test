# Generated by Django 2.2.10 on 2020-05-29 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('miembro', '0002_auto_20200528_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro',
            name='cliente_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cliente.Cliente'),
        ),
        migrations.AlterField(
            model_name='miembro',
            name='grupo_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='miembros', to='grupo.Grupo'),
        ),
    ]