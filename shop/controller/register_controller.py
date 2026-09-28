from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password

from shop.model.user_model import User


def register(request):

    if request.method == "POST":

        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        gender = request.POST.get("gender")
        address = request.POST.get("address")
        city = request.POST.get("city")

        existing_email = User.objects.filter(
            email=email
        ).first()

        if existing_email:
            return render(
                request,
                "shop/register.html",
                {
                    "error": "Email already registered."
                }
            )

        existing_phone = User.objects.filter(
            phone=phone
        ).first()

        if existing_phone:
            return render(
                request,
                "shop/register.html",
                {
                    "error": "Phone number already registered."
                }
            )

        # Securely hash the password
        hashed_password = make_password(password)

        User.objects.create(
            full_name=full_name,
            email=email,
            phone=phone,
            password=hashed_password,
            gender=gender,
            address=address,
            city=city
        )

        return redirect("/login/")

    return render(request, "shop/register.html")