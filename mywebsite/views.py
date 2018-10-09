from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect

def index(request):
    return HttpResponse("welcome to Django programming.")

def home(request):
    if request.method=='GET':
        if "user" in request.GET:
            if request.GET['user']=='logout':
                if 'username' in request.session:
                    del request.session['username']
        if 'username' not in request.session:
            return redirect('/blogs/user/login/')
            # return render(request, 'user_form/user_login.html')


        return HttpResponse("<h1>This is my home page-<a href='?user=logout'>logout</a></h1>")