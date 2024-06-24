from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.helper.constants import bedroom_choices, price_choices, state_choices 
# Create your views here.


# def index(request):
#     return HttpResponse('<h1>This is an http response for index</h1>')
def index(request):
    latest_listings = Listing.objects.order_by("-list_date").filter(is_published=True)[:3]
    context = {
        "latestListings" : latest_listings,
        "bedroom_choices" : bedroom_choices,
        "price_choices" : price_choices,
        "state_choices" : state_choices
    }
    return render(request, "pages/index.html", context)


def about(request):
    # get all realtors
    realtorsArr = Realtor.objects.order_by("-hire_date")

    # get MVP realtor
    mvp_realtors = Realtor.objects.all().filter(is_mvp = True)
    context  = {
        'realtors' : realtorsArr,
        'mvp_realtors' : mvp_realtors
    }

    return render(request, "pages/about.html", context)


# def listings(request):
#     return render(request, 'pages/listings.html')


def test(request):
    return HttpResponse(
        """
                            <h1>This is an http response for test</h1>
                            <h1>This is 2nd line</h1>
                        """
    )


# def template(request):
#     return render(request, 'home/myhome.html')
