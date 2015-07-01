from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from stat_tracker.forms import LoginForm, RegistrationForm
from django.contrib.auth.models import User
from users.models import Profile

class IndexView(TemplateView):

    def get(self, request):
        form = LoginForm()
        registration_form = RegistrationForm()
        context = self.get_context_data()
        context['form'] = form
        context['registration_form'] = registration_form
        return render(request, 'index.html', context)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, \
                            password=password)

        response = HttpResponse()

        if user is not None:
            login(request, user)
            response.status_code = 200
            return redirect('#/activities')
        else:
            response.status_code = 404
            return redirect('#/login-error')


def register(request):
    respones = HttpResponse()

    if request.method == 'POST':
        form = RegisterForm(request.data)
        if form.is_valid():
            form.save(commit=False)
            inp = {'username': form.username,
                   'password': form.password,
                   'email': form.email}

            if not User.objects.filter(username=form.username).exists():
                user = User.objects.create(**inp)
                Profile.objects.create(user=user)
                return redirect('#/activities')
            else:
                response = HttpResponse('Username already in use.')
                response.status_code = 400
                return response
        else:
            response = HttpResponse(form.errors)
            response.status_code = 400
            return response

    response.status_code = 405
    return response
