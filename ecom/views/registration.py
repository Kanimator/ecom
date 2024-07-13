from django.contrib.auth.views import LoginView

class CustomerLoginView(LoginView):
    authentication_form = None
