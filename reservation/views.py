from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from listing.models import ParkingSpace


def information(request, id):
    space = get_object_or_404(ParkingSpace, pk=id)
    return render(request,
                  "reservation/space_info.html",
                  {'space': space}
                  )