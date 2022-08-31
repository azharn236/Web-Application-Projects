from.models import Person

def menu_links(request):
    links = Person.objects.all()
    return dict(links=links)
