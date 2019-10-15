from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


class ContextMixin(object):
    context = {

    }

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context.update(self.context)
        return context

class PaginationMixin(object):
    '''quick and dirty mixin to support pagination on filterviews '''
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        if not self.queryset and hasattr(self, 'get_queryset'):
            self.queryset = self.get_queryset()
            
        filter = self.filterset_class(self.request.GET, queryset=self.queryset)
        object_list = filter.qs
        
        
        if not self.paginate_by:
            self.paginate_by = 20

        p = Paginator(object_list, self.paginate_by)

        page_str = self.request.GET.get('page')
        try:
            page = p.page(page_str)
        except PageNotAnInteger:
            #gets first page
            page = p.page(1)
        except EmptyPage:
            #gets last page 
            page = p.page(p.num_pages)

        context['object_list'] = page
        context['paginator'] = p
        context['is_paginated'] = True
        context['page_obj'] = page

        return context