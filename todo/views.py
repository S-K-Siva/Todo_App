from django.shortcuts import render,redirect
from django.http import HttpResponse
#Class Based View ->ListView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import CreateView,UpdateView,DeleteView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.
from .models import TodoList

class TaskList(LoginRequiredMixin,ListView):
    model = TodoList
    template_name = 'todo/todolist.html'
    context_object_name = 'listobject'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['listobject'] = context['listobject'].filter(user=self.request.user)
        context['complete'] = context['listobject'].filter(complete=False)

        search = self.request.GET.get("search-text")
        if search:
            context['listobject'] = context['listobject'].filter(title__icontains=search)
            context['search-text'] = search
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = TodoList
    context_object_name = 'listdetail'
    template_name = 'todo/tododetail.html'



class CreateTask(LoginRequiredMixin,CreateView):
    model = TodoList
    fields = ['title','description','complete']
    template_name = 'todo/createlist.html'
    #context_object_name = 'createlist'
    success_url = reverse_lazy('Task')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask,self).form_valid(form)

class UpdateTask(LoginRequiredMixin,UpdateView):
    model = TodoList
    fields = ['title','description','complete']
    template_name = 'todo/updatelist.html'
    success_url = reverse_lazy('Task')
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UpdateTask,self).form_valid(form)


class DeleteTask(LoginRequiredMixin,DeleteView):
    model = TodoList
    template_name = 'todo/deletetask.html'
    success_url = reverse_lazy('Task')

class LoginPage(LoginView):
    model = TodoList
    template_name = 'todo/login.html'
    success_url = reverse_lazy('Task')

    def get_success_url(self):
        return reverse_lazy('Task')



class RegisterView(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('Task')
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('Task')
        return super(RegisterView,self).get(*args,**kwargs)




