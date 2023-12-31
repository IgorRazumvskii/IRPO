from django.contrib.auth import login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView, TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from .models import Animal, Shelter
from .forms import AnimalCreateForm, ShelterCreateForm, RegistrationForm


#  список питомцев
class AnimalList(ListView):
    model = Animal
    template_name = 'animal_list.html'
    context_object_name = 'animals'
    paginate_by = 15


#  представление одного питомца
class AnimalDetail(DetailView):
    model = Animal
    template_name = ''
    context_object_name = 'animal'


#  создание питомца
class AnimalCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_animal'
    model = Animal
    form_class = AnimalCreateForm
    template_name = 'animal_create.html'
    success_url = reverse_lazy('')

    def form_valid(self, form):
        animal = form.save(commit=False)
        animal.shelter = Shelter.objects.get(user=self.request.user)
        return super().form_valid(form)


#  удаление питомца
class AnimalDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'app.add_animal'
    model = Animal
    template_name = ''
    context_object_name = 'animal'
    success_url = reverse_lazy('')


#  представление кабинета приюта
class ShelterCabinet(TemplateView):
    template_name = ''


#  создание приюта
class ShelterCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'app.add_shelter'
    model = Shelter
    form_class = ShelterCreateForm
    template_name = 'shelter_create.html'
    success_url = reverse_lazy('animal_create')

    def form_valid(self, form):
        shelter = form.save(commit=False)
        shelter.user = self.request.user
        return super().form_valid(form)


# список питомцев приюта
class ShelterAnimalList(ListView):
    model = Animal
    template_name = 'shelter_animals_list.html'
    context_object_name = 'animals'
    paginate_by = 15

    # ToDo: check
    def get_queryset(self):
        queryset = super().get_queryset()
        shelter = Shelter.objects.get(user=self.request.user)
        return queryset.filter(shelter=shelter)


#  представление кабинета пользователя
class UserCabinet(TemplateView):
    template_name = ''


# регистрация для простых пользователей
def sign_in(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('animal_list')

    else:
        form = RegistrationForm()
    return render(request, 'user_registration.html', context={'form': form})





