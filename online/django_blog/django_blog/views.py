from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.http import require_http_methods

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(
        request,
        'index.html',
        context={'who': 'world'},
    )

def index(request):
    return render(
        request,
        'index.html',
        context={'who': 'world'},
    )


def about(request):
    tags = ['программировние', 'tag2', 'tag3']
    return render(
        request, 
        'about.html', 
        context={'tags': tags}
    )

#@require_http_methods(["GET", "POST"])
# def login(request):
#     if request.method == "GET":
#         return render(
#             request, "login_page.html", context={"username": request.GET["username"]}
#         )
#     elif request.method == "POST":
#         username = request.POST["username"]
#         password = request.POST["password"]
#         check_password(username, password)
#         ...


# def med_info_view(request, user_id, pet_id):
#     ...