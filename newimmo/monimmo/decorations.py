from django.shortcuts import redirect
from django.http import HttpResponse
from .models import Programme

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_funct(request, *args, **kargs):
            group = None
            if request.user.groups.exist:
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kargs)
            else:
                return HttpResponse("Vous n'êtes pas autorisé à accéder à cette page")
        return wrapper_funct
    return decorator


def have_reservation(view_func):
    def wrapper_funct(request, *args, **kargs):
        user_id = request.user.pk
        programOwners = Programme.objects.values_list('owner', flat=True)
        if user_id in programOwners :
            return view_func(request, *args, **kargs)
        else :
            return HttpResponse("Vous n'êtes pas autorisé à accéder à cette page")
    return wrapper_funct



