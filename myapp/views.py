from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from django.http import HttpResponseBadRequest
from .models import TodoModel

def TodoList(request):
    todo = TodoModel.objects.all()
    contex = {
        'todo':todo
    }
    return render(request, 'index.html',contex)

@require_POST
def toggle_completed(request, todo_id):
    todo = get_object_or_404(TodoModel, id=todo_id)
    completed = request.POST.get('completed')
    if completed is None:
        return HttpResponseBadRequest('Missing completed value')
    todo.completed = completed == 'true' or completed == 'on' or completed == '1'
    todo.save()
    return redirect(request.META.get('HTTP_REFERER', '/'))