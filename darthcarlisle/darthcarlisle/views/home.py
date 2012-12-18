from django.http import HttpResponse
from django.views.generic import View

class HomeView(View):

	def get(self, request, *args, **kwargs):
		return HttpResponse('Hello, World!')