from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from shop.model.user_model import User


def profile(request):

    user_id = request.session.get("user_id")

    if not user_id:
        return redirect("/login/")

    user = User.objects.filter(user_id=user_id).first()

    if not user:
        return redirect("/login/")

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        city = request.POST.get("city")
        password = request.POST.get("password")

        user.full_name = full_name
        user.email = email
        user.phone = phone
        user.gender = gender
        user.address = address
        user.city = city

        if password:
            user.password = make_password(password)

        user.save()

        request.session["user_name"] = user.full_name

        return redirect("/profile/")

    return render(
        request,
        "shop/profile.html",
        {
            "user": user
        }
    )


def logout(request):

    request.session.flush()

    return redirect("/login/")