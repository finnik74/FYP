from .models import Userinfo


def auth_user(uinfo):
    uname = uinfo.get('name')
    results = {'status': 'fail', 'message': ''}
    user_query = Userinfo.objects.filter(name=uname)
    if len(user_query) == 0:
        results['message'] = 'User name is not valid'
    else:
        for user in user_query:
            if user.password == uinfo.get('password'):
                results['status'] = 'success'
                results['message'] = 'Authentication Succeeded!'
            else:
                results['message'] = 'Password is not right'
    return results

def auth_register(uinfo):
    uname = uinfo.get('name')
    results = {'status': 'fail', 'message': 'User has existed.'}
    user_query = Userinfo.objects.filter(name=uname)
    if len(user_query) == 0:
        results['status'] = 'success'
        results['message'] = 'Register successfully!'
    return results

