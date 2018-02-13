from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from gallery.models import Gallery, Photo


def post_list(request):
    posts = Gallery.objects.filter(published_date__lte=timezone.now()).order_by('my_order')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Gallery, slug=slug)
    return render(request, 'post_detail.html', {'post': post})

def contact(request):
    return render(request, 'contact.html', {})