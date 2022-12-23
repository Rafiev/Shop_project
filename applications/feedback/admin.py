from django.contrib import admin

from applications.feedback.models import Comment, Like

admin.site.register(Comment)
admin.site.register(Like)