#from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Image
import random
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect

class Index(generic.ListView):
    template_name = 'facemash/index.html'
    context_object_name = 'image_list'
    def get_queryset(self):
        im1 = Image.objects.all()
        im=[]
        im2=[]
        sel = random.randint(0,len(im1)-1)
        im.append(im1[sel])
        im2 = im1[:sel]+im1[(sel+1):]
        sel1 = random.randint(0,len(im2)-1)
        im.append(im2[sel1])
        return im[:2]
    

def selected(request):
    if(request.method == "POST"):
        img = get_object_or_404(Image, pk=request.POST['choice'])
        img.point += 1
        img.save()
        return HttpResponseRedirect(reverse('facemash:index'))
    else:
        return redirect('Index.as_view()')
