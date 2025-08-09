from django import forms
from .models import Task 

class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'priority', 'deadline']
        widgets = {
            'deadline': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
                    }        
        

class TaskFilterForm(forms.Form):
    STATUS_CHOICES = [
        ('', 'All'),
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ]

    PRIORITY_CHOICES = [
        ('', 'All'),
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Status', required=False)
    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, label='Priority', required=False)

    def __init__(self, *args, **kwargs):
        super(TaskFilterForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({"class": "form-control"})
