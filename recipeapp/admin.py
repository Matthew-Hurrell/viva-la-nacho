from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'method']
    list_filter = ('status', 'created_on', 'featured')
    list_display = ('title', 'slug', 'author', 'created_on', 'status', 'featured')
    summernote_fields = (
        'method',
        'ingredients',
    )
    actions = ['add_featured', 'remove_featured']

    def add_featured(self, request, queryset):
        queryset.update(featured=True)

    def remove_featured(self, request, queryset):
        queryset.update(featured=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    search_fields = ['recipe', 'name', 'body']
    list_filter = ('recipe', 'name', 'created_on', 'approved')
    list_display = ('name', 'email', 'recipe', 'created_on', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
