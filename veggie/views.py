from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

@login_required(login_url='/login/')
def recipes(request):
    if request.method=='POST':

        data = request.POST
        recipe_name=data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')
        
        # print(recipe_name)
        # print(recipe_desc)
        # print(recipe_img)

        Recipe.objects.create(
            recipe_name = recipe_name,
            recipe_desc = recipe_desc,
            recipe_img = recipe_img
            )
       
       
        return redirect('/recipes/')


    queryset = Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    
    
    
    context ={'recipes': queryset}
    return render(request, 'recipe.html', context)

@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()


    return redirect('/recipes/')

@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method=='POST':
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_desc = data.get('recipe_desc')
        recipe_img = request.FILES.get('recipe_img')

        queryset.recipe_name = recipe_name
        queryset.recipe_desc = recipe_desc
        if recipe_img:
            queryset.recipe_img = recipe_img

        queryset.save()
        return redirect('/recipes/')
    


    context ={'recipes': queryset}


    return render(request, 'update_recipe.html', context)


def login_page(request):

     if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/recipes/')

     return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def signup_page(request):

    if request.method =='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect('/signup/')
            
        

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )

        user.set_password(password)
        user.save()

        messages.info(request, 'Account created successfully ')
        return redirect('/signup/')


    return render(request, 'signup.html')



from django.db.models import Q, Sum

def get_student(request):
    queryset = Student.objects.all()

    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(student_name__icontains = search) |
            Q(department__department__icontains = search) |
            Q(student_id__student_id__icontains = search) |
            Q(student_email__icontains = search) |
            Q(student_age__icontains = search) 
            
            )
    
    paginator = Paginator(queryset, 11)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'report/students.html', {'queryset': page_obj})

# def get_student(request):
#     queryset = Student.objects.all

#     paginator = Paginator(queryset, 10)
#     page_number = request.GET.get('page', 1)
#     page_obj = paginator.get_page(page_number)


#     return render(request, 'report/students.html',  { 'queryset': page_obj})

from .fakeData import generateReport_card

def see_marks(request, student_id):
    # generateReport_card()
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum('marks'))
    current_rank = -1
    ranks = Student.objects.annotate(marks=Sum('studentmarks__marks')).order_by('-marks', 'student_age')
    i = 1
    for rank in ranks:
        if student_id == rank.student_id.student_id:
            current_rank=i
            break
        i = i +1
    return render(request, 'report/see_marks.html', {'queryset': queryset, 'total_marks': total_marks, 'current_rank':current_rank})