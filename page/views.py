from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from gallery.models import Gallery, Photo
from page.forms import ContactForm


def post_list(request):
    posts = Gallery.objects.filter(published_date__lte=timezone.now()).order_by('my_order')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, slug, id):
    post = get_object_or_404(Gallery, slug=slug, id=id)
    photo = Photo.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'post_detail.html', {'post': post, 'photo': photo})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    form_class = ContactForm
    return render(request, 'contact.html', {'form': form_class, })

