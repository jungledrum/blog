from django.shortcuts import redirect


def login_required(f):
    def decorator(req, *args, **kwargs):
        if req.session.get('username', None) == 'bo':
            return f(req, *args, **kwargs)
        else:
            return redirect('/admin')
    return decorator