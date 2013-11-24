This project actually a fork of datatables_demo 1.6.2 which is work with Django 1.5.1 and below. For more information checkout [1].

Django-Datatables
=======

Datatables-Datatables is a demonstration of the jQuery plug in, datatables with server side datasource from Django. The demonstration contains a working demoDjango project complete with HTML, CSS and Javascript needed to implement a complete working same.

How To Run This Demo?
======

    $ cd datatables_demo
    $ python manage.py runserver 8080

Usage
======

To implement this code into your application, follow these steps:

Create an entry in urls.py and views.py that will server the HTML and JS needed for datatables
Create a separate url and view for returning a json object to datatables.

    def get_surveys(request):
    querySet = Survey.objects.all()
    columnIndexNameMap = { 0: 'id', 1 : 'name', 2: 'description', 3: 'active', 4: 'created' }
    jsonTemplatePath = 'qa/survey/json_surveys.txt'
    return get_datatables_records(request, querySet, columnIndexNameMap, jsonTemplatePath)

1. Create a  queryset object for the model you wish the data to be drawn from (querySet)
2. Create a dict for the column names, in correct display order (columnIndexNameMap)
3. Return the response to get_datatables_records which is contained in utils.py

[1]: http://www.assembla.com/code/datatables_demo/subversion/nodes/trunk/1_6_2
