from django.shortcuts import render

# Create your views here.

# user type view function

def usertype_index(request):
    ''' this function displays all the data of usertype '''
    return render(request)

def usertype_create(request):
    ''' this function create form for usertype '''
    return render(request)

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
