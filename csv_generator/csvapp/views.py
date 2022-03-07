from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

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
    content = {
        'title': "Mind Risers | Django Class",
        'description': 'Poush Session Evening Group',
        'total_students': '10 Students in total'
    }
    return render(request, template, content)

def usertype_store(request):
    ''' this function stores all the data of usertype '''
    return render(request)
    
def usertype_edit(request, id):
    ''' this function displays data by it the data of usertype '''
    return render(request)
    
def usertype_update(request):
    ''' this function displays all the data of usertype '''
    return render(request)
    
def usertype_delete(request, id):
    ''' this function removes specific data of usertype '''
    return render(request)
        
def usertype_show(request, id):
    ''' this function displays data by it the data of usertypee '''
    return render(request)
