from django.db import models
from django.db.models import permalink
from datetime import datetime

from ckeditor.fields import RichTextField


class Blog(models.Model):
	title = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100, unique=True)
	body = RichTextField()
	writer = models.CharField(max_length=100, default='Akshat Uppal')
	posted = models.DateField(db_index=True, auto_now_add=True)
	category = models.ForeignKey('blog.Category')
	date = models.DateTimeField(default=datetime.now, blank=True)


	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return('view_blog_post', None, { 'slug' : self.slug })


class Category(models.Model):
	title = models.CharField(max_length=100, db_index=True)
	slug = models.SlugField(max_length=100, db_index=True)

	def __unicode__(self):
		return '%s' % self.title

	@permalink
	def get_absolute_url(self):
		return ('view_blog_category', None, { 'slug': self.slug })
