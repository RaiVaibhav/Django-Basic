from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserChangeForm
from accounts.forms import RegistrationForm
from django.contrib.auth.models import User
# Create your views here.
# Django has two type of view
#   - Function base view
#   - Class based view (complicated)

def home(request):
    #return HttpResponse('Home Page!')
    name = 'Vaibhav Rai'
    numbers = [1,2,3,4,5]
    args = {'myName': name,'numbers': numbers }
    return render(request, 'accounts/home.html', args)
    #name the template because of naming I have
    #created the accounts folder in templates folder
    # what Django will do by default id it will look into template folder for any html file
    #we created a "base.html" and this gone be included on every single page on a webpage of our project
    #and it will appear on every single page.
    #but it become like hard coded for every page like the things whic we don't want on our
    #will be get shown on our page
    #so too prevent that we use {% block head %}
def register(request):
    if request.method =='POST':
        form  = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('/account')
        #if request method is 'POST' means user is sending data to web server
        #if request method is 'GET' it means the data/page from web server

    else:
        form = RegistrationForm()
        args = {'form':form}
        return render(request, 'accounts/reg_form.html', args)

def view_profile(request):
    args = {'user': request.user}
    return render(request, 'accounts/profile.html',args)

def edit_profile(request):
    if request.method =='POST':
        form = UserChangeForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
            return redirect('/account/profile')

    else:
        form = UserChangeForm(instance = request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)





























