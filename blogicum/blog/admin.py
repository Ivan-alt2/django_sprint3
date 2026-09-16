from django.contrib import admin

from .models import Category, Post, Location


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Админка для публикаций."""

    list_display = (
        'title',
        'author',
        'pub_date',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    list_editable = ('category',)
    
    search_fields = ('title', 'text')
    list_filter = (
        'category', 
        'author', 
        'is_published', 
        'location'
    )
    list_display_links = ('title',)
    empty_value_display = '-пусто-'
    autocomplete_fields = ('author', 'location', 'category')
    date_hierarchy = 'pub_date'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Админка для категорий."""

    list_display = (
        'title',
        'description_preview',
        'is_published',
        'created_at',
    )
    search_fields = ('title', 'description')
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    empty_value_display = '-пусто-'
    prepopulated_fields = {"slug": ("title",)}

    def description_preview(self, obj):
        return (
            f'{obj.description[:40]}...'
            if len(obj.description) > 40 else obj.description
        )
    description_preview.short_description = 'Описание'


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    """Админка для местоположений."""

    list_display = ('name', 'is_published', 'created_at')
    search_fields = ('name',)
    list_filter = ('is_published',)
    list_editable = ('is_published',)
    empty_value_display = '-пусто-'
