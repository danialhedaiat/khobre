from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, CreateUserForm

# Create your views here.
from .models import Books, Category


class Login(View):
    template = "Login.html"
    formClass = LoginForm

    def get(self, request, *args, **kwargs):
        return render(request=request, template_name=self.template, context={"form": self.formClass})

    def post(self, request, *args, **kwargs):
        form = self.formClass(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
        msg = "Login failed!"
        return render(request, self.template, context={'form': self.formClass, "msg": msg}, status=401)


class CreateUser(View):
    template = "CreateUser.html"
    formClass = CreateUserForm

    def get(self, request, *args, **kwargs):
        form = self.formClass()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.formClass(request.POST)
        if form.is_valid():
            form.save(commit=False)


class Home(View):
    template = "Home.html"

    def get(self, request, *args, **kwargs):
        books = Books.objects.filter(rented=False)
        category = Category.objects.all()
        data = {"books": books,
                "category": category}
        return render(request, self.template, data)

    def post(self, request, *args, **kwargs):
        books = Books.objects.filter()
        return JsonResponse({"books": books})


class Search(View):

    def get(self, request, *args, **kwargs):
        book = Books.objects.get()
        return JsonResponse({"book": book})
