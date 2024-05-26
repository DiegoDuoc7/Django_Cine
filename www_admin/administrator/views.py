from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
TEMPLATE_DIRS = [
    os.path.join(BASE_DIR, 'templates'),
]

# Create your views here.
def index(request):                    #  <<==========
    return render(request,"index.html")      #  <<==========