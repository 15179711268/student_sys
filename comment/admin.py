from django.contrib import admin
from typeidea.custom_site import custom_site
from typeidea.base_admin import BaseOwnerAdmin

from . models import Comment
# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')