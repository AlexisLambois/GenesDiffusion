import json,sys
from django.http import Http404, HttpResponse

def go_insert(request):
        data = {'message': "%s added" % request.POST.get('filepath')}
        return HttpResponse(json.dumps(data), content_type='application/json')