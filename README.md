#javascript requirements

- datatables
- jquery

# how to install

```
pip install django-datatables-pagination
```
# example 

ListView

```python
class MyListView(DtPaginatedListView):
    model = MyModel
    tr_template = 'core/tr.html'
    # searchable fields 
    filtered_fields = ('id', 'field1', 'fiild2')
```

tr.html

```html
<td>{{object.id}}</td>
<td>{{object.field2}}</td>
<td>{{object.field2}}</td>
```

mymodel_list.html

```html
{% block content %}
    <table class="datatable">
        <tr>
            <th>id</th>
            <th>field1</th>
            <th>field2</th>
        </tr>
    </table>
{% endblock %}

{% block scripts %}
    {% include 'django_datatables_pagination/datatables_setup.html' %}
{% endblock %}
```
