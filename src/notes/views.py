from django.shortcuts import render, get_object_or_404, redirect

from .models import Note
from .forms import NoteForm

def note_list_view(request):
    form=NoteForm()
    if request.method == "POST":
        form = NoteForm(request.POST)
        print(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            return redirect('note-list')
    to_do_list = Note.objects.filter(finished=False)
    finished_list = Note.objects.filter(finished=True)
    context ={
        "to_do_list": to_do_list,
        "finished_list" : finished_list,
        'form': form
    }
    return render(request,'note_list.html', context)

def finished_task(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished=True
    note.save()
    return redirect('note-list')

def recover_item(request, id):
    note = get_object_or_404(Note, id=id)
    note.finished = False
    note.save()
    return redirect("note-list")

def deleted_task(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('note-list')

