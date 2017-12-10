from django.contrib import admin
from blog.models import Blog, Category


class BlogAdmin(admin.ModelAdmin):
	list_display = [ "writer", "category", "date"]
	list_filter = ["category", "date", "title"]
	search_fields = ["title", "body"]
	exclude = ['posted']
	prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
	list_display = ["__unicode__", "slug"]
	prepopulated_fields = {'slug': ('title',)}


admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

