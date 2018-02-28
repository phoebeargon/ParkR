from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.shortcuts import render

from listing.models import ParkingSpace


# Create your views here.
@login_required()
def profile(request):
    spaces = ParkingSpace.objects.filter( owner=request.user )
    return render(request, 'account/profile.html', {'owned_spaces': spaces})


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = "account/signup_form.html"
    success_url = reverse_lazy('parkr_home')
