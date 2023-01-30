# Generated by Django 4.0.5 on 2022-06-21 10:08

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('m_menus', '0004_globalmenu_footer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='globalmenu',
            name='footer',
            field=wagtail.fields.StreamField([('Page', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.PageChooserBlock())])), ('Item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.CharBlock(default='#'))]))], use_json_field=None),
        ),
    ]
