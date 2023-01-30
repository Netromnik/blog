# Generated by Django 4.0.5 on 2022-06-19 13:33

from django.db import migrations
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('m_menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='globalmenu',
            name='munus',
            field=wagtail.fields.StreamField([('Page', wagtail.blocks.StructBlock([('href', wagtail.blocks.PageChooserBlock())])), ('Item', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('href', wagtail.blocks.CharBlock(default='#'))]))], default=0, use_json_field=None),
            preserve_default=False,
        ),
    ]
