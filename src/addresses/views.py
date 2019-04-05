from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import AddressRegisterForm

# Create your views here.


def addressregister(request):
    if request.method == 'POST':
        form = AddressRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your address has been created! ')
            return redirect('profile')
    else:
        form = AddressRegisterForm()
    return render(request, 'addresses/address_form.html', {'form': form})
