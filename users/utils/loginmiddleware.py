from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

class UserTypeRedirectMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Get the user type
            user_type = request.user.user_type
            print("user type",user_type)

            # Define redirect URLs for each user type
            redirect_urls = {
                'AdminUser': reverse('dashboard'),  # Replace 'admin_dashboard' with your URL name
                'Donor': reverse('index'),      # Replace 'donor_dashboard' with your URL name
            }

            # Check if the response is a redirect to the login page
            if response.status_code == 302 and 'login' in response['Location']:
                # Redirect based on user type
                return redirect(redirect_urls.get(user_type, 'default_dashboard'))  # Replace 'default_dashboard' with your URL name if needed

        return response
