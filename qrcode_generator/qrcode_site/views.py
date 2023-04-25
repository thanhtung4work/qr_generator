from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from . import utils

# Create your views here.
def index(request):
  template = loader.get_template('index.html')
  return render(request, "index.html")

def get_qr(request):
  if request.method == "POST":
    input_text = request.POST.get('input_text')
    return HttpResponse(utils.generate_qr(input_text))