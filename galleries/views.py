from django.views.generic.list_detail import object_list,object_detail
from boundless.django.galleries.models import Gallery, Photo

RESULTS_PER_LIST_PAGE=50

def index(request, page=1):
    qs = Gallery.objects.all()

    return object_list(request, queryset=qs, template_object_name='gallery',\
        paginate_by=RESULTS_PER_LIST_PAGE, page=page)

def gallery(request, identifier, slugified=False):
    data = {
        'queryset': Gallery.objects.all()
    }

    if slugified == False:
        data['object_id'] = identifier
    else:
        data['slug'] = identifier

    return object_detail(request, template_object_name='gallery', **data)

def photo(request, identifier, slugified=False):
    data = {
        'queryset': Photo.objects.all()
    }

    if slugified == False:
        data['object_id'] = identifier
    else:
        data['slug'] = identifier

    return object_detail(request, template_object_name='photo', **data)

