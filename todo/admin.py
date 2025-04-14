from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    search_fields = ["name"]
    list_filter = ["name"]
    ordering = ("name",)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    ordering = ("done", "-created_at",)

    fieldsets = (
        (("Additional info", {"fields": ("created_at", "done",)}),)
    )
    add_fieldsets = (
        (
            (
                "Additional info",
                {
                    "fields": (
                        "created_at",
                        "done",
                    )
                },
            ),
        )
    )
