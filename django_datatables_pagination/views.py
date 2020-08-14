from django.http import JsonResponse
from django.template.loader import render_to_string
from django.views.generic import ListView
from django.contrib.auth.context_processors import PermWrapper


def split_html_by_tds(html):
    """get a peace of html containing tds and returns the
        content of each td as a elemenent in a list"""

    splited_html = html.split('</td>')
    result = []
    for html_chunck in splited_html:
        striped_html_chunk = html_chunck.strip()
        if striped_html_chunk:
            arrow_right_index = striped_html_chunk.find('>')
            result.append(striped_html_chunk[arrow_right_index + 1:])

    return result


def filter_by_search_term(queryset, fields, search_term):
    new_queryset = queryset.none()
    for field in fields:
        new_queryset |= queryset.filter(**{f'{field}__icontains': search_term})
    return new_queryset


class DtPaginatedListView(ListView):
    tr_template = None
    filtered_fields = []

    def post(self, *args, **kwargs):
        start = int(self.request.POST.get("start"))
        length = int(self.request.POST.get("length"))
        search_term = self.request.POST.get("search[value]")
        draw = int(self.request.POST.get("draw"))

        queryset = self.get_queryset()
        records_total = queryset.count()

        if search_term:
            queryset = filter_by_search_term(queryset, self.filtered_fields, search_term)

        records_filtered = queryset.count()
        data = []
        queryset_page = queryset[start: start + length]

        for obj in queryset_page:
            html = render_to_string(
                self.tr_template, context={
                    'object': obj,
                    'user': self.request.user,
                    'perms': PermWrapper(self.request.user)})
            tds = split_html_by_tds(html)
            data.append(tds)

        return JsonResponse({
            "draw": draw,
            "recordsTotal": records_total,
            "recordsFiltered": records_filtered,
            "data": data})
