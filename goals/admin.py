from django.contrib import admin
from goals.models.category import Category
from goals.models.comment import Comment
from goals.models.goal import Goal


class GoalCategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created", "updated")
    search_fields = ("title", "user")


admin.site.register(Category, GoalCategoryAdmin)
admin.site.register(Goal)
admin.site.register(Comment)