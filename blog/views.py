from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    # fetch all data
    post_data = Post.objects.all()
    return render(request, "home.html", {"posts": post_data})