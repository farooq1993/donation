from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseForbidden

class UserTypeRedirectMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the user type
            user_type = request.user.user_type
            print("user type",user_type)

            # Define redirect URLs for each user type
            redirect_urls = {
                'AdminUser': reverse('dashboard'),  
                'Donor': reverse('index'),      
            }

            # Check if the response is a redirect to the login page
            if response.status_code == 302 and 'login' in response['Location']:
                # Redirect based on user type
                return redirect(redirect_urls.get(user_type, 'default_dashboard'))  
        return response



class RestrictDonorMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of CMS URLs to restrict
        cms_urls = [
            '/cms/',  
            '/admin/',
        ]

        # Check if the user is a 'Donor' and trying to access CMS URLs
        if request.path.startswith(tuple(cms_urls)):
            if request.user.is_authenticated and request.user.user_type == 'Donor':
                return HttpResponseForbidden("Donor do not have permission to access this page.")

        response = self.get_response(request)
        return response