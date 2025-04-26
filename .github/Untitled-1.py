# ... existing code ...
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("مرحباً بك في موقع Django!")