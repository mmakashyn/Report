# Generated by Django 3.2.7 on 2021-09-29 12:25

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseStudyListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote'], icon='pilcrow')), ('columns_content', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock())])), ('case_study', wagtail.core.blocks.StructBlock([])), ('columns', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote'], icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))], icon='fa-columns')), ('column3', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column4', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column6', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column8', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column9', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))]))], template='report/includes/content.columns.block.html'))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ReportPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote'], icon='pilcrow')), ('front_cover', wagtail.core.blocks.StructBlock([('cover_image', wagtail.images.blocks.ImageChooserBlock(help_text='Image to be used for the background of the cover block', icon='picture')), ('logo', wagtail.images.blocks.ImageChooserBlock(icon='picture')), ('title', wagtail.core.blocks.CharBlock()), ('links', wagtail.core.blocks.StreamBlock([('link', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock(max_length=100, min_length=1, required=True)), ('id', wagtail.core.blocks.CharBlock(max_length=100, required=True))]))]))])), ('columns_content', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.RichTextBlock())])), ('executive_summary', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.RichTextBlock()), ('content', wagtail.core.blocks.TextBlock())])), ('fullwidth_background_image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(icon='picture')), ('content', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote'], required=False)), ('columns', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote'], icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))], icon='fa-columns')), ('column3', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column4', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column6', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column8', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column9', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))]))]))], help_text='Web content displayed in the foreground (optional)', required=False))])), ('case_study', wagtail.core.blocks.StructBlock([])), ('columns', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote'], icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))], icon='fa-columns')), ('column3', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column4', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column6', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column8', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column9', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))]))], template='report/includes/content.columns.block.html'))], null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='CaseStudyPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('body', wagtail.core.fields.StreamField([('columns', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote'], icon='pilcrow')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('column', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))], icon='fa-columns')), ('column3', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column4', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column6', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column8', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))])), ('column9', wagtail.core.blocks.StreamBlock([('text', wagtail.core.blocks.RichTextBlock(features=['h2', 'h3', 'h4', 'h5', 'h6', 'bold', 'italic', 'ol', 'ul', 'hr', 'link', 'document-link', 'image', 'embed', 'code', 'superscript', 'subscript', 'blockquote', 'cm_blue', 'cm_orange', 'cm_red', 'cm_green'], icon='pilcrow')), ('logo_and_circle_image', wagtail.core.blocks.StructBlock([('logo', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('background_color', wagtail.core.blocks.CharBlock())])), ('person_name', wagtail.core.blocks.RichTextBlock()), ('short_description', wagtail.core.blocks.RichTextBlock(template='report/includes/content.short_description.html')), ('action_button', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(help_text='Text to be used for the button', required=False)), ('url', wagtail.core.blocks.URLBlock(help_text='Link URL'))])), ('collage', wagtail.core.blocks.ListBlock(wagtail.images.blocks.ImageChooserBlock())), ('theses', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock()), ('subtitle', wagtail.core.blocks.TextBlock())]))]))], template='report/includes/case-study.columns.block.html'))], null=True)),
                ('background_color', models.CharField(blank=True, help_text='Background color that should be used for the model viewer.', max_length=10, null=True)),
                ('person_name', models.CharField(blank=True, help_text='Title of the case study', max_length=1000, null=True)),
                ('description', models.CharField(blank=True, help_text='Description of the case study', max_length=2000, null=True)),
                ('featured', models.BooleanField(default=True)),
                ('cover', models.ForeignKey(blank=True, help_text='Image to be shown in the header of case study', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
