from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect, reverse, Http404
from django.views.generic import View

from .forms import ApplicationForm
from utils.generic import generate_applicationid, create_application, AppDetails, get_all_applications

# Create your views here.

class ApplicationAuthMixin(View):
    """
    Show application details to the user who applies it. Though there can be an exception for admins. :)
    """

    def dispatch(self, request, *args, **kwargs):
        applicationid = kwargs.get('applicationid')
        cookie_apps = request.COOKIES.get('applications') or ''
        # ToDo: Add an exception for Admin as admin can see this application details page.
        if applicationid not in cookie_apps:
            return HttpResponseRedirect(reverse('apply'))
        return super(ApplicationAuthMixin, self).dispatch(request, *args, **kwargs)


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
        # Though the application id is a very unique and very difficult to guess,
        # it's good to add the applicationid in the current user active session.
        cookie_apps = request.COOKIES.get('applications') or ''
        cookie_apps += ',' + applicationid
        response = HttpResponseRedirect(reverse('application', kwargs={'applicationid': applicationid}))
        response.set_cookie('applications', cookie_apps)
        return response


class ApplicationView(ApplicationAuthMixin, View):
    """
    Show applied application to the user who applied it!
    """

    def get(self, request, *args, **kwargs):
        applicationid = kwargs.get('applicationid')
        app_obj = AppDetails(applicationid)
        return render(request, 'application.html', {'application': app_obj.application})


class ListApplicationView(LoginRequiredMixin, View):
    """
    Show all applications from where logged in user can approve or reject the applications
    """

    def get(self, request, *args, **kwargs):
        all_applications = get_all_applications('first_name')
        # ToDo: add functionalities to 'accept' or 'reject' the applications
        return render(request, 'list_applications.html', {'applications': all_applications})


