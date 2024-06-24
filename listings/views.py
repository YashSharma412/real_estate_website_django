from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .helper.constants import bedroom_choices, price_choices, state_choices 
from .models import Listing

# Create your views here.
def index(request):
    # listings_arr = Listing.objects.all() # Listing model will fetch all listings from listing table in database
    listings_arr = Listing.objects.order_by("-list_date").filter(is_published=True)
    paginator = Paginator(listings_arr, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
        # "listings_arr": listings_arr
        "listings_arr": paged_listings,
    }
    return render(request, 'pages/listings.html', context)

def listing(request, listing_id):
    current_listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        "listing" : current_listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    queryset_list = Listing.objects.order_by("-list_date")
    context = {
        "listings_arr" : queryset_list,
        "bedroom_choices" : bedroom_choices,
        "price_choices" : price_choices,
        "state_choices" : state_choices
    }
    return render(request, 'listings/search.html', context)


# def listing(request):
#     return render(request, 'pages/listing.html') 