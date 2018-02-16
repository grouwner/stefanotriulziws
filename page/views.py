from email.message import EmailMessage

from django.conf import settings
from django.http import BadHeaderError, HttpResponse, HttpResponseServerError
from django.shortcuts import render, redirect
from django.template import Context, loader
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from gallery.models import Gallery, Photo
from page.forms import ContactForm
from django.core.mail import send_mail


def post_list(request):
    posts = Gallery.objects.filter(published_date__lte=timezone.now()).order_by('my_order')
    return render(request, 'home.html', {'posts': posts})

def post_detail(request, slug, id):
    post = get_object_or_404(Gallery, slug=slug, id=id)
    photo = Photo.objects.filter(gallery_id='15',published_date__lte=timezone.now()).order_by('published_date')
    #photo = get_object_or_404(Photo)
    #photo = Photo.objects.filter(author='prova')
    return render(request, 'post_detail.html', {'post': post, 'photo': photo})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    context = {}

    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_contact_mail(request)
            context["message_sended"] = True

    context["form"] = form

    return render(request, "contact.html", context)



