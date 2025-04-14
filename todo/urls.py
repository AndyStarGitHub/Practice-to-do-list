from django.urls import path

from .views import (index,
                    TagListView,
                    TagCreateView,
                    TagUpdateView,
                    TagDeleteView,
                    TaskCreateView,
                    TaskUpdateView,
                    TaskDeleteView,
                    task_toggle_done,
                    )

urlpatterns = [
    path("", index, name="index"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/",
         TagCreateView.as_view(),
         name="tag-add",),
    path(
        "tags/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update",
    ),
    path(
        "tags/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete",
    ),
    path("tasks/add/",
         TaskCreateView.as_view(),
         name="task-add",),
    path(
        "tasks/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update",),
    path(
        "tasks/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete",),
    path(
        "tasks/<int:pk>/toggle/",
        task_toggle_done,
        name="task-toggle-done",),
]

app_name = "todo"
