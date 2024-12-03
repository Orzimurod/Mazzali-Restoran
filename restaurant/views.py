from django.shortcuts import render, redirect
from django.contrib.auth import logout

from restaurant.models import About, GalleryImage, MenuItem, Slider, Chef

def index_view(request):
    sliders = Slider.objects.filter(is_active=True)
    about_data = About.objects.all()
    menu_items = MenuItem.objects.all()
    imgs = GalleryImage.objects.all()[:8]
    chefs = Chef.objects.all()[:3]

    context = {
        'sliders': sliders,
        'about_data': about_data,
        'menu_items': menu_items,
        'imgs': imgs,
        'chefs': chefs,
    }

    return render(request, 'index.html', context)


# def login_view(request):
#     return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('index')


# def register_view(request):
#     return render(request, 'register.html')