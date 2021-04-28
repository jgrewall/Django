from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse("Hello everyone! we did it!")

def showpage3(request):
    return render(request, 'index.html')


# def index(request):
    # return render(request, 'index.html')

# Create your views here.


#display methods:::::(redirect)
#def displayIndex(request,) 

#action methonds::::::(request)
#def sendHome(request):
#   return redirect('/')
