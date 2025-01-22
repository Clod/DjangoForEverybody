from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from autos.models import Auto, Make

# Create your views here.

class MainView(LoginRequiredMixin, View):
    def get(self, request):
        mc = Make.objects.count()
        al = Auto.objects.all()

        ctx = {'make_count': mc, 'auto_list': al}

        # The template autos/auto_list.html is rendered. Django looks for this template
        # in the autos/templates/autos/ directory.
        return render(request, 'autos/auto_list.html', ctx)


class MakeView(LoginRequiredMixin, View):
    def get(self, request):
        ml = Make.objects.all()
        ctx = {'make_list': ml}
        return render(request, 'autos/make_list.html', ctx)



# Take the easy way out on the main table
# These views do not need a form because CreateView, etc.
# Build a form object dynamically based on the fields
# value in the constructor attributes

# For CreateView and UpdateView, Django looks for a template named <model_name>_form.html.
# For DeleteView, Django looks for a template named <model_name>_confirm_delete.html.

'''

├── templates
│   └── autos
│       ├── auto_confirm_delete.html
│       ├── auto_form.html
│       ├── auto_list.html
│       ├── make_confirm_delete.html
│       ├── make_form.html
│       └── make_list.html

'''

class AutoCreate(LoginRequiredMixin, CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos:all')

class MakeCreate(LoginRequiredMixin, CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos:all')


