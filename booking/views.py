
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import generic
from .models import BookModel, OurUser
from .forms import BootstrapEventForm, XDSoftEventForm, FengyuanChenEventForm, DateForm


def get_booker(user):
    qs = OurUser.objects.filter(user=user)
    if qs.exists():
        return qs[0]
    return None

class HomeView(generic.TemplateView,LoginRequiredMixin):
    model = BookModel
    template_name = 'core/home.html'
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        book = BookModel.objects.all()
        context = super().get_context_data(**kwargs)
        context['book'] = book       
        return context


class DetailView(LoginRequiredMixin, generic.DetailView):
    model = BookModel
    template_name = 'core/event_detail.html'
    context_object_name = 'queryset'


class BookCreate(LoginRequiredMixin, generic.CreateView):
    model = BookModel
    form_class = XDSoftEventForm
    template_name = 'core/xdsoft_event_form.html'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Create'
        return context

    def form_valid(self, form):
     
        form.instance.ouruser = get_booker(self.request.user)
        form.save()
        messages.success(self.request, 'Successfully booked your  car')
        return redirect(reverse("booking:book-detail", kwargs={
            'pk': form.instance.pk
        }))
    
    


class BookEdit(LoginRequiredMixin, generic.UpdateView):
    model = BookModel
    form_class = XDSoftEventForm
    template_name = 'core/xdsoft_event_update_form.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update'
        return context
        
    def form_valid(self, form):
        form.instance.ouruser = get_booker(self.request.user)
        form.save()
        messages.success(self.request, 'Successfully updated your  car')
        return redirect(reverse("booking:book-detail", kwargs={
            'pk': form.instance.pk
        }))

        

class BookDelete(LoginRequiredMixin, generic.DeleteView):
    model = BookModel
    template_name = 'core/book_delete.html'

    def get_success_url(self):
        messages.success(self.request, 'Form info deleted successfully!')
        return reverse('booking:home')




