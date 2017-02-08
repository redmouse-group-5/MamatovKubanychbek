from django.contrib import admin
from blog.models import Post
from comment.models import Comments



def make_change_publish(modeladmin, request, queryset):
    for o in queryset:
        o.publish = not o.publish
        o.save()
make_change_publish.short_description = "Revert publish"

def make_published(modeladmin, request, queryset):
    queryset.update(publish=True)
make_published.short_description = "Mark selected stories as published"

def make_unpublished(modeladmin, request, queryset):
    queryset.update(publish=False)
make_unpublished.short_description = "Mark selected stories as unpublished"

class CommentsInline(admin.TabularInline):
    model = Comments

class PostAdmin(admin.ModelAdmin):
    actions = [make_change_publish, make_published, make_unpublished]
    actions_on_top = True
    actions_on_bottom = True
    actions_selection_counter = True
    date_hierarchy = 'created_date'
    # exclude = ['publish', ]
    readonly_fields = ['publish', 'created_date', 'date_update', 'author']
    # fields = ['title',]
    fieldsets = (
        (None, {
            'fields': ('title', 'text',)
        }),
        ('Advanced options', {
            'classes': ('collapse', 'extrapretty'),
            'description': "Дата публикации",
            'fields': ('author', 'image', 'publish')
        }),
        ('Date options', {
            'classes': ('collapse', 'extrapretty'),
            'description': "Дата публикаци:",
            'fields': ('created_date', 'date_update')
        }),
    )
    inlines = [
        CommentsInline,
    ]
    list_display = ('title', 'author', 'created_date', 'date_update', 'publish')
    list_display_links = ('title', 'created_date', 'date_update')
    list_editable = ('publish', )
    list_filter = ('author', 'publish', 'created_date')
    # list_per_page = 1
    # list_max_show_all = 3
    ordering = ('title', )
    # radio_fields = {"author": admin.HORIZONTAL}
    # raw_id_fields = ('author', )
    save_as = True
    search_fields = ('title', 'text')
    view_on_site = True

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)

# Register your models here.
