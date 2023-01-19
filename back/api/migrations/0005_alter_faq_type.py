# Generated by Django 4.1.4 on 2022-12-29 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_faq_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='type',
            field=models.CharField(choices=[('MAIL', 'Mail'), ('JESLASTIC', 'Jelastic'), ('SWISSBACKUP', 'Swissbackup'), ('NEWSLETTER', 'Newsletter'), ('BILLETERIE', 'Billeterie'), ('PUBLICCLOUD', 'Publiccloud'), ('KDRIVE', 'Kdrive'), ('KCHAT', 'Kchat'), ('CALENDRIER', 'Calendrier'), ('VOD/AOD', 'Vod/Aod'), ('SERVERCLOUD', 'Servercloud'), ('DOMAINES', 'Domaines'), ('SSL', 'Ssl'), ('WORKSPACE', 'Workspace')], default='MAIL', max_length=50),
        ),
    ]