from django.shortcuts import render, HttpResponse, redirect, render
from .models import User, Message, Comment
import bcrypt
from django.contrib import messages
from django.contrib.messages import get_messages

def index(request):
    if ('userID' in request.session):
        return redirect('/success')
    return render(request, "theWall.html")
def displaysuccess(request):
    if (('userID' not in request.session)):
        return redirect('/')
    context={
        'all_messages':Message.objects.all(),
        'thisUser':User.objects.get(id=request.session['userID'])
    }
    return render(request, "success.html", context)

def newUser(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        pw_hash=bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()

        newUser = User.objects.create(firstName=request.POST['fName'],lastName=request.POST['lName'],email=request.POST['email'], password=pw_hash)
        messages.success(request, " successfully updated")

        request.session['userID']=newUser.id
        return redirect('/success')

def login(request):
    errors=User.objects.login_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    #get user wrapped in array if filter(), if get() its not in
    user = User.objects.filter(email=request.POST['email'])
    #get that user in that array
    logged_user= user[0]
    if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
        request.session['userID']=logged_user.id
        return redirect('/success')
    else:
        messages.error(request, 'email or password invalid')
        return redirect('/')

#clear the session and redirect to logout
def logout(request):
    request.session.clear()
    return redirect('/')


def message(request):
    errors=User.objects.message_validator(request.POST)
    if len(errors)>0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    message=Message.objects.create(
        #user = is "user.object.get()" because its a ForeignKey
        user=User.objects.get(id=request.POST['userID']),
        message=request.POST['textBoxMessage'])
    user = User.objects.get(id=message.user_id)
    user.messages.add(message)
    return redirect('/success')

def comment(request):
    comment = Comment.objects.create(
        message=Message.objects.get(id=request.POST['messageID']),
        user=User.objects.get(id=request.POST['userID']),
        comment=request.POST['textBoxComment'])
    message = Message.objects.get(id=comment.message_id)
    message.comments.add(comment)
    return redirect('/success')