from .models import Masjid
from django.urls.base import reverse

from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.views.generic import DetailView
from django.views.generic import ListView

from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

class MasjidList(ListView):
    template_name = "list.html"
    model = Masjid


class MasjidCreate(CreateView):
    template_name = "home.html"
    model = Masjid
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        print(form.cleaned_data['masjid_name'])
# <bound method BaseModelForm.clean of <MasjidForm bound=True, valid=True, fields=(masjid_name;city;country;method;masjidLogo)>>
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class MasjidEdit(UpdateView):
    template_name = "home.html"
    model = Masjid
    fields = '__all__'


class MasjidDelete(DeleteView):
    template_name = "delete.html"
    model = Masjid
    success_url = reverse_lazy('masjid_list')


class MasjidDetail(DetailView):
    template_name = "detail.html"
    model = Masjid
    fields = '__all__'
