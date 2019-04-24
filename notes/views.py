from django.shortcuts import render, redirect

from .models import DailyNote, WeeklyNote
from .forms import DailyNoteEdit, WeeklyNoteEdit

def daily_update(request, pk):
    if request.method == 'POST':
        note = DailyNote.objects.get(pk=pk)
        form = DailyNoteEdit(instance=note, data=request.POST)

        if form.is_valid():
            form.instance.created_by = note.created_by
            form.instance.valid_date = note.valid_date

            pending_form = form.save(commit=False)
            if request.user.is_authenticated:
                pending_form.updated_by = request.user

                pending_form.save()

    return redirect('welcome:index')

def weekly_update(request, pk):
    if request.method == 'POST':
        note = WeeklyNote.objects.get(pk=pk)
        form = WeeklyNoteEdit(instance=note, data=request.POST)

        if form.is_valid():
            form.instance.created_by = note.created_by
            form.instance.start_date = note.start_date

            pending_form = form.save(commit=False)
            if request.user.is_authenticated:
                pending_form.updated_by = request.user

                pending_form.save()

    return redirect('welcome:index')