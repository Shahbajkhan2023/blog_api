from django.forms import BaseModelForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views import View
from django.http import HttpResponse, JsonResponse
from .forms import ProfileUpdateForm, PostForm
from .models import Post
from django.urls import reverse_lazy
from .tasks import send_email_to_users


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['user_profile'] = self.request.user.profile
            context['form'] = ProfileUpdateForm(instance=self.request.user.profile)
            print(f'Context==== {context}')
        return context


class ProfileUpdateView(View):
    def post(self, request, *args, **kwargs):
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': 'profile updated successfully!'})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        response = super().form_valid(form)
        # Celery taks call
        send_email_to_users.delay(form.instance.title)
        return response
    
    def form_invalid(self, form):
        return JsonResponse({'success': False, 'errors': form.errors}, status=400)
    
    