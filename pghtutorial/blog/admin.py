from django.contrib import admin
from .models import Post

@admin.register(Post)
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "author", "created", "updated") #lista aparecendo mais informações do post
    prepopulated_fields = {"slug": ("title",)} #o slug vai sendo escrito junto com o titulo