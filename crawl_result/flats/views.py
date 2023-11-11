from django.shortcuts import render
from flats.models import Flat
from django.core.paginator import Paginator

def list_flats(request):
    """Handles paging and generating the view from the data."""
    latest_flat_list = Flat.objects.all()
    paginator = Paginator(latest_flat_list, 20)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'flats/list.html', {'page_obj': page_obj})
