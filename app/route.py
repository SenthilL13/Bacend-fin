from chatAssist import py_ChatAssist
from login_signup import py_login_signup
from services import py_services


def ch_login(request):
    response = py_login_signup.fn_login_user(request)
    return response


def ch_signup(request):
    response = py_login_signup.fn_signup_user(request)
    return response


def ch_chat_assist(request):
    response = py_ChatAssist.fn_chat_assist(request)
    return response


def ch_services_management(request):
    response = py_services.fn_services_management(request)
    return response


def ch_user_management(request):
    response = py_services.fn_user_management(request)
    return response
