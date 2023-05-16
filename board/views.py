from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from django.contrib.auth import authenticate, login
from .forms import UserForm
from django.http import HttpResponse


def index(request):
    # 게시물 목록 출력
    postList = Post.objects.order_by('-date')
    context = {'postList': postList}
    return render(request, 'board/list.html', context)

def detail(request, postId):
    # 상세보기
    post = Post.objects.get(id=postId)
    context = {'post': post}
    return render(request, 'board/detail.html', context)

def answer_create(request, postId):
    # 답글 추가
    post = get_object_or_404(Post, pk=postId)
    post.answer_set.create(content=request.POST.get('content'), date=timezone.now())
    return redirect('board:detail', postId=postId)

def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})