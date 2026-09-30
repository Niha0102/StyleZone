from django.shortcuts import redirect


def entry(request):

    if request.session.get('user_id'):
        return redirect('home')

    return redirect('login')