# Generated by Django 4.0.5 on 2022-06-19 13:36

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('m_menus', '0002_globalmenu_munus'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalmenu',
            name='site_name',
            field=models.CharField(default='Netro.fun', max_length=120),
        ),
        migrations.AlterField(
            model_name='globalmenu',
            name='munus',
            field=wagtail.fields.StreamField([('Page', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.PageChooserBlock())])), ('Item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.CharBlock(default='#'))]))], use_json_field=None),
        ),
    ]
