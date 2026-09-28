from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password

from shop.model.user_model import User


def login(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        user = User.objects.filter(
            email=email
        ).first()

        if user and check_password(password, user.password):

            request.session["user_id"] = user.user_id
            request.session["user_name"] = user.full_name

            return redirect("/")

        return render(
            request,
            "shop/login.html",
            {
                "error": "Invalid email or password"
            }
        )

    return render(request, "shop/login.html")