from django.shortcuts import render, redirect
from .forms import ReservationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def reservation_view(request):
    message = None
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            message = "Joyingiz muvaffaqiyatli band qilindi!"
            return redirect('index') 
        else:
            message = "Iltimos, formani to'ldirib qayta yuboring."
    else:
        form = ReservationForm() 

    return render(request, 'index.html', {'form': form, 'message': message})
