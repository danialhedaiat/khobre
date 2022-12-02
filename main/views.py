from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.views import View
from .forms import LoginForm, CreateUserForm

# Create your views here.
from .models import Books, Category, User


class Login(View):  # this class not wanted in the task
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
                return redirect('Home')
        msg = "Login failed!"
        return render(request, self.template, context={'form': self.formClass, "msg": msg}, status=401)


class CreateUser(View):
    template = "CreateUser.html"
    formClass = CreateUserForm

    def get(self, request, *args, **kwargs):
        # render create user html file with clear form to creating user
        form = self.formClass()
        return render(request, self.template, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.formClass(request.POST)
        if form.is_valid():  # check validation of form
            try:  # use try to prevent any errors during the user creating
                messages.success(request, "your user created!")
                form.save()
                return redirect('Home')
            except Exception as e:
                messages.error(request, e) # if any error catch, send error message to html
                return render(request, self.template, {'form': form})
        else:
            messages.error(request, form.errors)  # if form was not valid, send error message to html
            return render(request, self.template, {'form': form})


class Home(View):
    template = "Home.html"

    def get(self, request, *args, **kwargs):
        # render home page with all books and send categories for filtering
        books = Books.objects.all()
        category = Category.objects.all()
        data = {"books": books,
                "category": category}
        return render(request, self.template, data)

    def post(self, request, *args, **kwargs):
        # get filtering request for home page
        data = dict()
        rented = bool(request.POST["rented"])
        category = request.POST["category"]
        if rented:
            data["rented"] = False
        if category:
            data["category"] = category
        books = Books.objects.filter(**data)
        content = render_to_string("table.html", {"books": books})
        return JsonResponse({"content": content})


class Search(View):

    def post(self, request, *args, **kwargs):
        # search books by they name
        if request.POST['name']:
            books = Books.objects.filter(name__startswith=request.POST['name'])
        else:
            books = Books.objects.all()
        content = render_to_string("table.html", {"books": books})
        return JsonResponse({"content": content})
