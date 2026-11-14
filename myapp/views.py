from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm

def user_list(request):
    records = User.objects.all().order_by('-id')
    context = {
        'records': records,
        'total_count': records.count(),
    }
    return render(request, 'Listingpage.html', context=context)

def AddUser(request):
    form = UserForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form}
    return render(request, 'Add.html', context)

def EditUser(request, id=None):
    one_rec = get_object_or_404(User, pk=id)
    form = UserForm(request.POST or None, request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form, 'user': one_rec}
    return render(request, 'Edit.html', context=context)

def DeleteUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    if request.method == "POST":
        one_rec.delete()
        return redirect('/')
    context = {'user': one_rec}
    return render(request, 'Delete.html', context=context)

def ViewUser(request, eid=None):
    one_rec = get_object_or_404(User, pk=eid)
    context = {'user': one_rec}
    return render(request, 'View.html', context=context)
