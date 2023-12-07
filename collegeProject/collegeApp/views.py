from django.shortcuts import render, redirect
from django.contrib import messages
#from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PersonCreationForm
from .models import Department, Course,Students,chkboxcourse
# Create your views here.

def index(request):
    return render(request,'index.html')
def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            materials_provide=request.POST.get('materials_provide')
            print(materials_provide)
            savedata = Students(
                name=form.cleaned_data['name'],
                dob=form.cleaned_data['dob'],
                age=form.cleaned_data['age'],
                gender=form.cleaned_data['gender'],
                phone_number=form.cleaned_data['phone_number'],
                mail_id=form.cleaned_data['mail_id'],
                address=form.cleaned_data['address'],
                department=form.cleaned_data['department'],
                course=form.cleaned_data['course'],
                purpose=form.cleaned_data['purpose'],
                materials_provide=materials_provide,
            )
            savedata.save()
            messages.success(request, 'Form Submitted Successfully')
            return redirect('person_add')

    return render(request, 'home.html', {'form': form})

# AJAX
def load_courses(request):
    # print(request.GET)
    # print("s")
    department_id = request.GET.get('department_id')
    print(department_id)
    courses = Course.objects.filter(department_id=department_id)
    print(list(courses.values('id', 'name')))
    return render(request, 'city_dropdown_list_options.html', {'courses': courses})
    # return JsonResponse(list(courses.values('id', 'name')), safe=False)

def person_update_view(request, pk):
    person = get_object_or_404(Students, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':

        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})

# def savevalues(request):
#     if request.method=='POST':
#         if request.POST.get('materials_provide'):
#             savedata=chkboxcourse()
#             savedata.materials_provide=request.POST.get('materials_provide')
#             savedata.save()
#             return render(request, 'home.html')
#     else:
#         return render(request,'home.html')

# def person_create_view(request):
#     form = PersonCreationForm()
#     if request.method == 'POST':
#         form = PersonCreationForm(request.POST)
#         if form.is_valid():
#
#             materials_provide=request.POST.get('materials_provide')
#
#             if request.POST.get('materials_provide'):
#                Students.objects.create(materials_provide=materials_provide)
#                savedata = Students()
#                savedata.materials_provide = request.POST.get('materials_provide')
#                savedata.save()
#             student = form.save(commit=False)
#             student.save()
#             # student.materials_provide.set(materials_provided)
#             return redirect('person_add')
#     return render(request, 'home.html', {'form': form})