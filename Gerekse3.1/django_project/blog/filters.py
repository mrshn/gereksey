import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    CHOICES = (
            ('ascending', 'ESKİDEN YENİYE'),
            ('descending', 'YENİDEN ESKİYE')
            )
    
    ordering =  django_filters.ChoiceFilter(label='Sıralama', choices=CHOICES, method='filter_by_order')
    
    class Meta:
        model = Post
        fields = ['Kategori_1', 'Kategori_2']
        #fields = {
               # 'fields':['icontains']
                #}
    
    def filter_by_order(self, queryset, name, value):
        expression = 'date_posted' if value == 'ascending' else '-date_posted'
        return queryset.order_by(expression)
        