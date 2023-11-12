
from datetime import datetime


class TitleMixin:
    title = None
    store_name = 'Sash'
    current_date = datetime.now().year

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['store_name'] = self.store_name
        context['current_date'] = self.current_date
        return context
