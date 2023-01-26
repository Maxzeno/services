from django.shortcuts import render
from django.views import View

# Create your views here.

class Index(View):
	def get(self, request):
		return render(request, 'index.html', {})

	# def post(self, request):
	# 	data = dict(request.POST)
	# 	data.pop('csrf_token')

	# 	product = Product.objects.filter(tracking_code=trackcode).first()
	# 	if product:
	# 		return render(request, 'tracking1.html', {'product': product})
	# 	return redirect('/tracking.php?track=invalidcode')


