from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

from stat_tracker.forms import LoginForm


class IndexView(TemplateView):

    def get(self, request):
        form = LoginForm()
        context = self.get_context_data()
        context['form'] = form
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
