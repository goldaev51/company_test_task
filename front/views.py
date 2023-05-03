from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from .forms import TaskForm
from .models import Task


class TaskListView(generic.ListView):
    """
    TaskListView представляет собой список всех задач, отсортированных по дате создания.
    """
    model = Task
    template_name = 'front/task_list.html'
    context_object_name = 'tasks'
    ordering = ['-creation_time']


class TaskDetailView(generic.DetailView):
    """
    TaskDetailView отображает полную информацию о задаче, включая заголовок, описание, дату создания и статус (выполнена или нет).
    """
    model = Task
    template_name = 'front/task_detail.html'


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    """
    TaskCreateView предоставляет форму для создания новой задачи с полями для ввода заголовка, описания и даты выполнения задачи.
    """
    model = Task
    template_name = 'front/task_create.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('front:task_detail', args=[self.object.pk])


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    """
    TaskUpdateView предоставляет форму для редактирования существующей задачи, включая изменение заголовка, описания и даты выполнения.
    """
    model = Task
    template_name = 'front/task_update.html'
    form_class = TaskForm

    def get_success_url(self):
        return reverse('front:task_detail', args=[self.object.pk])


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    TaskDeleteView предоставляет страницу для подтверждения удаления задачи.
    После удаления задачи пользователь перенаправляется на страницу со списком задач.
    """
    model = Task
    template_name = 'front/task_delete.html'
    success_url = reverse_lazy('front:task_list')


class TaskToggleStatusAPI(generic.View):
    """
    TaskToggleStatusAPI является API-классом для изменения статуса задачи на выполненную или невыполненную.
    Обновление статуса происходит в фоновом режиме без перезагрузки страницы.
    """

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs['pk'])
        task.status = not task.status
        task.save()
        return JsonResponse({'status': task.status})
