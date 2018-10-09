from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,redirect

# from .models import StudentPortal
from . import models
from . import forms



# Create your views here.
def blog_index(request):
    # return HttpResponse("<h1>This blog page</h1>")
    return render(request, 'home/index.html')


def new_user(request):
    return render(request, 'user_form/user_registration.html')

def user_form_login(request):
    st_form=forms.StudentPortalLoginForm()
    context={
        "st_form":st_form
    }
    return render(request,'user_form/user_form_login.html',
                  context)

def user_login(request):
    if request.method=='GET':
        if 'username' in request.session:
            request.session['username']
            # username=request.session['username']
            # print("Session user name:",username)
            return redirect('/home/')
        return render(request, 'user_form/user_login.html')

    if request.method == 'POST':
        uname = request.POST['username']
        pword = request.POST['password']

        u_object = models.StudentPortal.objects.filter(user_email=uname)

        if len(u_object)< 1 or pword != u_object[0].user_pass:

            # return HttpResponseRedirect('/blog/user/login/')
            return redirect('/blogs/user/login/',msg="User id or Password is wrong")

        # if pword!=u_object[0].user_pass:
        #     return HttpResponseRedirect('/blog/user/login/')

        # print("User credentials: \n"
        #       "User name:",uname,"\n",
        #       "User password:",pword)
        request.session['username']=uname

        return HttpResponseRedirect('/home/')


def user_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        psw = request.POST['psw']
        print("Name:", name, "Email:", email, "Pass:", psw)

        st_obj = models.StudentPortal()
        st_obj.user_name = name
        st_obj.user_email = email
        st_obj.user_pass = psw
        st_obj.save()

    return HttpResponse("<h1>Data saved.</h1>")


def bootstrap(request):
    return render(request, 'home/home.html')


def student_list(request):
    st_list = models.StudentPortal.objects.all()
    context = {
        "student_list": st_list
    }
    return render(request, 'user_form/student_list.html', context={"key": "Student List", "student_list": st_list}
                  )
