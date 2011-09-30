class Paginator(object):
    """ Paginates queryset by per_page items per page """
    def __init__(self, queryset=None, page=1, per_page=10):
        self.queryset = queryset
        self.page = page
        self.per_page = per_page
        self.items_count = self.queryset.count()
        
        self.page_count = self.items_count / self.per_page
        if self.items_count % self.per_page != 0:
            self.page_count += 1
    
    def object_list(self):
        return self.queryset.offset((self.page-1)*self.per_page) \
                            .limit(self.page*self.per_page).all()
    
    def page_list(self, adjacent_pages=3):
        if self.page_count == 1:
            return []
        
        left_index = self.page - adjacent_pages - 1
        if left_index < 0:
            left_index = 0
        right_index = self.page + adjacent_pages
        
        return range(1, self.page_count + 1)[left_index:right_index]


def paginate(request, queryset, per_page=10):
    """ Takes request and queryset and returns paginated object_list """
    page = request.GET.get('page', 1)
    try:
        page = int(page)
    except ValueError:
        page = 1

    return Paginator(queryset, page, per_page)
