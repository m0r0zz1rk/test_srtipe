from django.views.generic import TemplateView


class ItemsList(TemplateView):
    template_name = 'list.html'