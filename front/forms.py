from django import forms

from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'due_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
        }
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'due_date': 'Дата выполнения',
        }
