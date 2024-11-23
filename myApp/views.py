from django.shortcuts import render

# Function to render the home page
def home(request):
    # Context can include dynamic data if needed
    context = {
        'welcome_message': 'Welcome to Saferide!',
    }
    return render(request, "myApp/home.html", context)
