from django.shortcuts import render
from django.utils import timezone
from .models import post
from django.shortcuts import get_object_or_404
# Create your views here.

def post_list(request):
    posts=post.objects.filter(published__lte=timezone.now()).order_by('published_date')
    return render(request,'blog/post_list.html',{'post':posts})
