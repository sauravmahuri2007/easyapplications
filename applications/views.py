from django.shortcuts import render, HttpResponseRedirect, reverse, Http404
from django.views.generic import View

from .forms import ApplicationForm
from utils.generic import generate_applicationid, create_application, AppDetails

# Create your views here.

class LoginView(View):
    # ToDo: create a login form and the a login template
    pass

class ApplyView(View):
    """
    Create an application submitted by the user
    """

    def get(self, request, *args, **kwargs):
        form = ApplicationForm()
        return render(request, 'home.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        post_params = request.POST.copy()
        form = ApplicationForm(post_params)
        if not form.is_valid():
            return render(request, 'home.html', context={'form': form})
        applicationid = generate_applicationid()
        app_data = form.cleaned_data
        app_data['applicationid'] = applicationid
        create_application(app_data)
        return HttpResponseRedirect(reverse('application', kwargs={'applicationid': applicationid}))


class ApplicationView(View):
    """
    Show application
    """

    def get(self, request, *args, **kwargs):
        applicationid = kwargs.get('applicationid')
        app_obj = AppDetails(applicationid)
        return render(request, 'application.html', {'application': app_obj.application})


