from django.shortcuts		import render_to_response
from django.template		import RequestContext

def homepage(request):
	subscription = dict()
	subscription = {'created_at' : '18/03/2012', 'phone' : '24-22336258', 'email': 'eventex@eventex.com',}
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))
