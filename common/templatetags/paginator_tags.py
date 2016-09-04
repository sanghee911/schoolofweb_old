"""
 Written by Sanghee Lee on 2016/07/22
 This inclusion tag uses template named 'paginator.html'.
 The paginator keeps 9 pages and first, last, prev, next buttons.
"""
from django import template

register = template.Library()


@register.inclusion_tag('common/paginator.html', takes_context=True)
def get_pagination(context):
    page_obj = context['page_obj']
    paginator = context['paginator']
    is_paginated = context['is_paginated']
    total_pages = paginator.num_pages
    current_page = page_obj.number
    total_range = range(1, total_pages + 1)
    queries = context.get('queries')

    # if pages less than 10, display all pages
    if total_pages < 10:
        page_range = range(1, total_pages + 1)

    # if pages more than 9 or equal to 10, change page range
    else:
        # keeps 4 pages in the front and back
        start_page = current_page - 4
        end_page = current_page + 4

        # if start page is negative, change to 1
        if start_page < 1:
            start_page = 1

        # if last page's number is bigger than total pages, change to total pages number
        if end_page > total_pages:
            end_page = total_pages

        page_range = range(start_page, end_page + 1)

        # keeps 9 pages
        if len(page_range) < 9:
            if 1 in page_range:
                page_range = total_range[:9]
            elif total_pages in page_range:
                page_range = total_range[-9:]

    return {
        'paginator': paginator,
        'page_obj': page_obj,
        'page_range': page_range,
        'is_paginated': is_paginated,
        'total_pages': total_pages,
        'current_page': current_page,
        'queries': queries,
    }



