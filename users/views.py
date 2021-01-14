from djnago.views import View
from django.shortcuts import render


class LoginView(View):
    def get(self, reqeust):
        return render(request, "users/login.html")

    def post(self, request):
        pass