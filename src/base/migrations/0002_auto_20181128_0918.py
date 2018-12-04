# Generated by Django 2.1.3 on 2018-11-28 08:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StandardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.core.fields.StreamField([('section_blocks', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.TextBlock()), ('heading', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.TextBlock()), ('link', wagtail.core.blocks.TextBlock(required=False))])), ('link', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('icon', wagtail.core.blocks.TextBlock())])), ('project_link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock()), ('summary', wagtail.core.blocks.TextBlock())])), ('paragraph', wagtail.core.blocks.RichTextBlock(template='blocks/paragraph_block.html'))], blank=True, null=True, verbose_name='Page Body')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='footertext',
            name='body',
            field=wagtail.core.fields.StreamField([('section_blocks', wagtail.core.blocks.StructBlock([('icon', wagtail.core.blocks.TextBlock()), ('heading', wagtail.core.blocks.TextBlock()), ('content', wagtail.core.blocks.TextBlock()), ('link', wagtail.core.blocks.TextBlock(required=False))])), ('link', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('icon', wagtail.core.blocks.TextBlock())])), ('project_link', wagtail.core.blocks.StructBlock([('link', wagtail.core.blocks.URLBlock()), ('summary', wagtail.core.blocks.TextBlock())])), ('paragraph', wagtail.core.blocks.RichTextBlock(template='blocks/paragraph_block.html'))], verbose_name='Body'),
        ),
    ]