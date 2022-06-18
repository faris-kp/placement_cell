from django.shortcuts import render
from django.views.generic import View

# Create your views here.
class Index(View):
    template_name = 'placement/index.html'

    def get(self,request):
        return render(request, self.template_name)

    def post(self,request):
        pass