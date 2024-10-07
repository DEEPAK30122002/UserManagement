from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import User
from django.db.models import Q
from .forms import UserForm
from . import models

# Create and Update
def user_create_or_update(request, id=None):
    if id:
        user = get_object_or_404(User, id=id)
    else:
        user = None
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'users/user_form.html', {'form': form})

# Read (list all users)

def user_list(request):
    query = request.GET.get('q')
    if query:
        user_list = User.objects.filter(
            Q(first_name__icontains=query) | 
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        user_list = User.objects.all()
    
    paginator = Paginator(user_list, 10)  # Paginate the result
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    
    return render(request, 'users/user_list.html', {'users': users, 'query': query})

# Delete
def user_delete(request, id):
    user = get_object_or_404(User, id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_list')
    return render(request, 'users/user_confirm_delete.html', {'user': user})
