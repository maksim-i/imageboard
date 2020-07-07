from django.contrib import admin
from imageboard_app.models import Post, Reply

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject',)
    prepopulated_fields = {'slug': ('subject',)}

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'text',)

admin.site.register(Post, PostAdmin)
admin.site.register(Reply, ReplyAdmin)
