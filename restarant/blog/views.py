from django.shortcuts import render
from blog.models import Post
import markdown

def blog_home(request):
    posts = Post.objects.all()
    title = 'Blog. Home page'
    return render(request, 'home_blog.html', {'posts': posts, 'title': title})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    posts = Post.objects.all()
    html_content = markdown.markdown(post.content)
    
    return render(request, 'post_detail.html', {'post': post, 'posts': posts, 'html_content': html_content})