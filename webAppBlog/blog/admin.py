from django.contrib import admin
from blog.models import Post, PostCategory, Comment
from django.db import models
from django.forms import Textarea


@admin.register(PostCategory)
class PostCategoryAdmin(admin.ModelAdmin):
    # In order to allow the auto completion (in which field it will be made )
    search_fields = ['name']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
   
    # Fields to display in the list
    list_display = (
        'title',
        'category',
        'published',
        'created_at',
        'comments_count',
    )

    # Filter pane on the right
    list_filter = (
        'category__name',
        'published',
    )

    # Auto completion
    autocomplete_fields = ['category']

    # Override the textFields to be biiger than de defaut one.
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'row': 20, 'cols': 90})}
    }

    # New field comments_count to count the number of post
    def comments_count(self, obj):
        return Comment.objects.filter(post=obj).count()
    comments_count.short_description = 'Comments'



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Field to search
    search_fields = ['post__title', 'author_name']


    #Field to display:
    list_display = (
        'post',
        'author_name',
        'status',
        'moderation_text',
        'created_at',
        'text',
    )

    # Allow to edit directly in the list view
    list_editable = ('status', 'moderation_text')

    # Filter pane on the right
    list_filter = (
        'status',
    )