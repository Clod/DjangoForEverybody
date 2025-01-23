from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Test page just to be if routing is ok.
'''
urlpatterns = [
    # path("", views.myview),
    path("", views.sessfun),
]
'''
def myview(request):
    # Render index.html
    return render(request, "hello/index.html")

# :
def sessfun(request):
    # Get the current value of 'num_visits' from the session.
    # If 'num_visits' doesn't exist in the session, default to 0.
    # Then, increment the value by 1.
    num_visits = request.session.get('num_visits', 0) + 1

    # Update the session with the new value of 'num_visits'.
    # This ensures the session stores the latest visit count.
    request.session['num_visits'] = num_visits

    # Check if the number of visits exceeds 4.
    # If so, delete the 'num_visits' key from the session.
    # This effectively resets the visit count.
    if num_visits > 4:
        del(request.session['num_visits'])

    # Create an HttpResponse object with a plain text message.
    # The message includes the current visit count.
    resp = HttpResponse('Refresh the page to see the view count = ' + str(num_visits) + ' times. And go back to 1 after 5 times.')

    # Add a cookie for grading purposed.
    resp.set_cookie('my_name_is_cookie', 'And this is my content', max_age=1000)

    # Return the HttpResponse object to the client.
    # This sends the response back to the user's browser.
    return resp