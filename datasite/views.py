import os
from datasite.forms import MomentForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def welcome(request):
    return HttpResponse('<h1>welcome</h1>')

def moments_input(request):
    if __name__ == '__main__':
        if request.method == 'POST':
            form = MomentForm(request.POST)
        if form.is_valid():
            moment = form.save()
            moment.save()
            return HttpResponseRedirect(reverse('app.views.welcome'))
    else:
            form = MomentForm()
    PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request, os.path.join(PROJECT_ROOT, 'datasite/templates', 'moments_input.html'), {'form': form})
