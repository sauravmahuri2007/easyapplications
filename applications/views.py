from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import View

from .forms import ApplicationForm
from utils.generic import generate_applicationid, create_application, AppDetails, get_all_applications


class ApplicationAuthMixin(View):
    """
    Show application details to the user who applies it. Though there can be an exception for admins. :)
    """

    def dispatch(self, request, *args, **kwargs):
        applicationid = kwargs.get('applicationid')
        cookie_apps = request.COOKIES.get('applications') or ''
        if (request.user and request.user.is_authenticated) or (applicationid in cookie_apps):
            return super(ApplicationAuthMixin, self).dispatch(request, *args, **kwargs)
        return HttpResponseRedirect(reverse('apply'))


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
        return render(request, 'list_applications.html', {'applications': all_applications})


class ApplicationActionView(LoginRequiredMixin, View):
    """
    This view will take care for approval or rejection of the applications
    """

    def get(self, request, *args, **kwargs):
        referrer_url = request.META.get('HTTP_REFERER')
        applicationid = kwargs.get('applicationid')
        action = request.GET.get('action')
        if not action or not applicationid:
            # return to the Referrer URL from where the request came or the apply page
            if referrer_url:
                return HttpResponseRedirect(referrer_url)
            return HttpResponseRedirect(reverse('apply'))
        try:
            app_obj = AppDetails(applicationid)
            app_obj.set_status(action)
            return HttpResponseRedirect(referrer_url)
        except:
            return HttpResponseRedirect(reverse('apply'))


