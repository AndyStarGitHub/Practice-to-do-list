from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import DeleteView

from todo.models import Task, Tag


# Create your views here.
def index(request: HttpRequest) -> HttpResponse:
    num_tasks = Task.objects.count()
    num_tags = Tag.objects.count()
    context = {
        "num_tags": num_tags,
        "num_tasks": num_tasks,
        "task_list": Task.objects.all()
    }
    return render(request, "todo/index.html", context=context)


class TagListView(generic.ListView):
    model = Tag
    context_object_name = "tag_list"
    template_name = "todo/tag_list.html"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_form.html"


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")
    template_name = "todo/tag_confirm_delete.html"


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_form.html"


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todo:index")
    template_name = "todo/task_confirm_delete.html"


def task_toggle_done(request, pk):
    task = Task.objects.get(id=pk)
    if task.done == 1:
        task.done = 0
    else:
        task.done = 1
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:index"))
