from django.views.generic import ListView, DetailView
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import Post
from .forms import PostForm, ReplyForm

class IndexView(ListView):
    model = Post
    template_name = 'imageboard_app/index.html'

class PostView(DetailView):
    model = Post
    template_name = 'imageboard_app/post.html'

def new_thread(request):
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'imageboard_app/new_thread.html', context)

def reply(request, *args, **kwargs):
    date_added = kwargs.get('date_added')
    post = get_object_or_404(Post, date_added=
                             Post.objects.latest('date_added').date_added)
    new_reply = None
    if request.method != 'POST':
        reply_form = ReplyForm()
    else:
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            new_reply = reply_form.save(commit=False)
            new_reply.post = post
            reply_form.save()
            return redirect('/')

    return render(request, 'imageboard_app/reply.html', {'post': post,
                                                     'new_reply': new_reply,
                                                     'reply_form': reply_form,})
