from importlib.metadata import requires
from django.shortcuts import render
from django.http import HttpResponse

# model class import
from csvapp.models import CsvUser

# form class import 
from csvapp.form import UserTypeForm
from csvapp.form import CsvUserLoginForm, CsvUserRegisterForm
# Create your views here.

# user view funtion
def user_login(request):
    template = 'users/login.html'
    ul = CsvUserLoginForm()
    if request.method == "POST":
        # method one
        # email = request.POST['email']
        # mehod two
        try:
            email = request.POST.get('email')
            password = request.POST.get('password')
            
            # fetching user object from database
            user = CsvUser.objects.get(email=email)
            if password is user.password:
                context = {
                    'form': ul,
                    'title': 'CSV | User Login',
                    'body_title': 'User Login',
                    'msg': 'Login success',
                    'user': user
                }
                return render(request, template, context)
            else:
                context = {
                    'form': ul,
                    'title': 'CSV | User Login',
                    'body_title': 'User Login',
                    'msg': 'Invalid email or password'
                }
                return render(request, template, context)
        except:
            context = {
                'form': ul,
                'title': 'CSV | User Login',
                'body_title': 'User Login',
                'msg': 'Not registered yet'
            }
            return render(request, template, context)
    else:
        context = {
            'form': ul,
            'title': 'CSV | User Login',
            'body_title': 'User Login',
            'msg': ''
        }
        return render(request, template, context)

def user_create(request):
    template = 'users/create.html'
    ur = CsvUserRegisterForm()
    context = {
        'title': 'CSV | Registration',
        'form': ur
    }
    if request.method == "POST":
        # taking post request data
        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        verification_code = request.POST.get('verification_code')
        is_active = request.POST.get('is_active')
        created_at = request.POST.get('created_at')

        user = CsvUser()
        user.first_name = first_name
        user.middle_name = middle_name
        user.last_name = last_name
        user.contact = contact
        user.email = email
        user.username = username
        user.password = password
        user.verification_code = verification_code
        user.is_verified = True
        user.is_active = is_active
        user.created_at = created_at
        # stores data in database
        user.save()
        context = {
            'title': 'CSV | Registration',
            'form': ur,
            'msg': 'Registered Successfully'
        }
        return render(request, template, context)
    else:
        return render(request, template, context)

# user type view function
def usertype_index(request):
    ''' this function displays all the data of usertype '''
    template = 'usertypes/index.html'
    content = {
        'title': "Usertype List",
        'description': {
            'id': 1,
            'usertype': 'UserAdmin',
            'status': 'active'
        }, 
        'num': range(10)
    }
    return render(request, template, content)

def usertype_create(request):
    ''' this function create form for usertype '''
    template = 'usertypes/create.html'
    utf = UserTypeForm
    content = {
        'title': "Mind Risers | Django Class",
        'description': 'Poush Session Evening Group',
        'total_students': '10 Students in total',
        'form': utf
    }
    return render(request, template, content)

def usertype_store(request):
    ''' this function stores all the data of usertype '''
    return render(request)
    
def usertype_edit(request, id):
    ''' this function displays data by it the data of usertype '''
    template = 'usertypes/edit.html'
    content = {
        'title': "Usertype List",
    }
    return render(request, template, content)
    
def usertype_update(request):
    ''' this function displays all the data of usertype '''
    return render(request)
    
def usertype_delete(request, id):
    ''' this function removes specific data of usertype '''
    template = 'usertypes/index.html'
    content = {
        'title': "Usertype List",
    }
    return render(request, template, content)
        
def usertype_show(request, id):
    ''' this function displays data by it the data of usertypee '''
    template = 'usertypes/show.html'
    content = {
        'title': "Usertype List",
    }
    return render(request, template, content)
