from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
#from collegeApp.forms import PersonCreationForm
from django.contrib import messages, auth

# Create your views here.
def register(request):
     if request.method== 'POST':
         username=request.POST['username']
         email=request.POST['email']
         password = request.POST['password']
         password1 = request.POST['password1']
         # user=User.objects.create_user(username=username,password=password,email=email)
         # user.save()
         if password == password1:
             if User.objects.filter(username=username).exists():
                 messages.info(request, "username taken")
                 return redirect('credentialApp:register')
             elif User.objects.filter(email=email).exists():
                 messages.info(request, "email taken")
                 return redirect('credentialApp:register')
             else:
                 user = User.objects.create_user(username=username,email=email, password=password)
                 user.save();
                 print("user created")
                 messages.info(request, "user created")
                 return redirect('credentialApp:login')
         else:
             messages.info(request, "password not matching")
             return redirect('credentialApp:register')
         # return render(request,'login.html')
     return render(request,'register.html')



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('credentialApp:dashboard')  # Redirect to the dashboard or another page
        else:
            # Handle authentication failure, e.g., display an error message
            messages.info(request,'invalid credentials')
    return render(request, 'login.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def Logout(request):
    auth.logout(request)
    return redirect('index')


# def form_page(request):
#     if request.method == 'POST':
#
#         return redirect('/')
# #     return render(request, 'form_page_new.html')
#
# def form_page(request):
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#             # Process the form data (save to database, send emails, etc.) if needed
#
#             return redirect('/')
#     else:
#         form = PersonCreationForm()
#
#     return render(request, 'form_page_new.html', {'form': form})
#
# def logout(request):
#     auth.logout(request)
#     return redirect('/')
