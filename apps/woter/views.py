from apps.woter.forms import WaterForm
from apps.woter.models import Water
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class WaterListView(ListView):
    model = Water
    template_name = 'water_app/water.html'
    context_object_name = 'water_delivery'


class WaterCreateView(CreateView):
    template_name = 'water_app/create_update_water.html'
    form_class = WaterForm
    success_url = '/'


class WaterUpdateView(UpdateView):
    form_class = WaterForm
    template_name = 'water_app/create_update_water.html'
    pk_url_kwarg = 'pk'
    success_url = '/'

    def get_queryset(self):
        return Water.objects.all()

    def form_valid(self, form):
        post = form.save(commit=False)
        post.save()
        return super().form_valid(form)

class WaterDeleteView(DeleteView):
    model = Water
    template_name = 'water_app/delete.html'
    success_url = '/'