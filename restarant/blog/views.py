from blog.forms import CommentForm
from django.shortcuts import get_object_or_404, render
from blog.models import Post
import markdown
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Comment

def blog_home(request):
    posts = Post.objects.all()
    title = 'Blog. Home page'
    return render(request, 'home_blog.html', {'posts': posts, 'title': title})


# def detail_post(request, post_id):
#     post = get_object_or_404(Post, pk=post_id)
#     posts = Post.objects.all()
#     comments = post.comment_post.filter(status=True)
#     html_content = markdown.markdown(post.content)
#     context = {'post': post, 'posts': posts, 'html_content': html_content, 'comments': comments}
#     return render(request, 'post_detail.html', context)

def detail_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.all()
    comments = post.comment_post.filter(status=True)
    html_content = markdown.markdown(post.content)
    comment_form = CommentForm()
    context = {'post': post, 'posts': posts, 'html_content': html_content, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'post_detail.html', context)


def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return HttpResponseRedirect(reverse('detail_post', args=[post_id]))

    return HttpResponseRedirect(reverse('detail_post', args=[post_id]))




