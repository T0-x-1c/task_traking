from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from task_system.forms import TaskForm
from .models import Task

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')
