from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def register_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if User.objects.filter(username=username).exists():
            return JsonResponse({
                "success": False,
                "message": "Username already exists"
            })

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return JsonResponse({
            "success": True,
            "message": "User registered successfully"
        })


@csrf_exempt
def login_user(request):
    if request.method == "POST":
        data = json.loads(request.body)

        user = authenticate(
            username=data.get("username"),
            password=data.get("password")
        )

        if user:
            login(request, user)
            return JsonResponse({
                "success": True,
                "message": "Login successful"
            })

        return JsonResponse({
            "success": False,
            "message": "Invalid credentials"
        })


def logout_user(request):
    logout(request)
    return JsonResponse({
        "success": True,
        "message": "Logged out successfully"
    })

