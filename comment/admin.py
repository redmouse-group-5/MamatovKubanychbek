from django.contrib import admin

from comment.models import Comments

class CommentsAdmin(admin.ModelAdmin):
    list_display = ('author', 'date', 'article', 'publish')
admin.site.register(Comments, CommentsAdmin)

# Register your models here.
