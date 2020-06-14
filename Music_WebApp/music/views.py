from django.http import HttpResponse


def index(request):
    return HttpResponse("<center><H3> Hey! That's music!</H3></center>")
