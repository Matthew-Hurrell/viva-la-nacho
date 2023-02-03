from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """
    Class for the Recipe section of the admin area. 
    Organises the display of posts as well as filtering, search and other custom methods.
    """

    # Prepopulated Slug Field
    prepopulated_fields = {'slug': ('title',)}

    # Search Fields
    search_fields = ['title', 'method']

    # List Filter
    list_filter = ('status', 'created_on', 'featured')

    # List Display Fields
    list_display = (
        'title',
        'slug',
        'author',
        'created_on',
        'status',
        'featured'
    )

    # Summernote Fields
    summernote_fields = (
        'method',
        'ingredients',
    )

    # Recipe Admin Area Functions
    actions = ['add_featured', 'remove_featured']

    # Add Featured Recipe Function
    def add_featured(self, request, queryset):
        queryset.update(featured=True)

    # Remove Featured Recipe Function
    def remove_featured(self, request, queryset):
        queryset.update(featured=False)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Class for the Comment section of the admin area. 
    Organises the display of posts as well as filtering, search and other custom methods.
    """

    # Search Fields
    search_fields = ['recipe', 'name', 'body']

    # List Filter
    list_filter = ('recipe', 'name', 'created_on', 'approved')

    # List Display Fields
    list_display = ('name', 'email', 'recipe', 'created_on', 'approved')

    # Comment Admin Area Function
    actions = ['approve_comments']

    # Approve Comments Function
    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
