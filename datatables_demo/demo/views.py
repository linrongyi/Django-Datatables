from django.shortcuts import render_to_response
from django.template.context import RequestContext
from demo.models import Country
from demo.utils import get_datatables_records
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render_to_response('demo/index.html', locals(), context_instance=RequestContext(request))


def load_once_demo_view(request):
    #get all Countries objects. 
    #One thing which is required in 'load once mode' is to somehow prepare list, queryset that can be iterated in
    #given template. Datatables will do the rest. 'countries' is passed in context to template (in this case by using locals())
    countries = Country.objects.all()
    return render_to_response('demo/load_once_editable_demo.html', locals(), context_instance=RequestContext(request))


def server_side_demo_view(request):
    #do not prepare data in view (as in  above view), data will be retrieved using ajax call (see get_countries_list below).
   return render_to_response('demo/server_side_demo.html', locals(), context_instance=RequestContext(request))


def get_countries_list(request):
    #prepare the params

    #initial querySet
    querySet = Country.objects.all()
    #columnIndexNameMap is required for correct sorting behavior
    columnIndexNameMap = { 0: 'id', 1 : 'name', 2: 'formal_name', 3: 'capital', 4: 'currency_code', 5: 'currency_name', 6: 'phone_prefix', 7: 'tld' }
    #path to template used to generate json (optional)
    jsonTemplatePath = 'demo/json_countries.txt'

    #call to generic function from utils
    return get_datatables_records(request, querySet, columnIndexNameMap, jsonTemplatePath)

from django.http import HttpResponse
import json


@csrf_exempt
def edit_cell(request):
    row_name = request.POST.get("row_name")

    a_item = Country.objects.get(name=row_name)
    col_name = request.POST.get("col_name")
    new_val = request.POST.get("value")
    old_val = getattr(a_item, col_name)
    setattr(a_item, col_name, new_val)
    a_item.save()
    #print u"|".join([row_name, col_name, old_val, getattr(a_item, col_name)])
    return HttpResponse(getattr(a_item, col_name), mimetype='application/javascript')


def ajax_test(request):
    return HttpResponse("fdfdffd", mimetype='application/javascript')