from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

class HomeView(View):
    """
    A view that handles requests to the home page.

    Attributes:
        None
    """

    def get(self, request):
        """
        Handles GET requests to the home page.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response object.
        """
        # Print the host of the request
        print(request.get_host())

        # Get the host of the request
        host = request.get_host()

        # Check if the request is local
        # This is important for conditional logic in templates or further processing
        # For example, you might want to show different content or features based on whether the request is local
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0

        # Create the context for the template
        context = {
            'installed': settings.INSTALLED_APPS,  # List of installed Django apps
            'islocal': islocal  # Boolean indicating if the request is local
        }

        # Render the home/templates/home/main.html template with the context
        return render(request, 'home/main.html', context)
