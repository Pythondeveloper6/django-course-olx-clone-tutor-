from django.shortcuts import render

# Create your views here.
from .models import Post , Comment
from .forms import PostForm , CommentForm



def post_list(request):
    all_posts = Post.objects.all()  # retrieve from models : db
    return render(request , 'all_posts.html' , {'posts' : all_posts})



def post_detail(request , id):
    post_detail = Post.objects.get(id=id)

    post_coments = Comment.objects.filter(post=post_detail)

    if request.method == 'POST' : 
        form = CommentForm(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.post = post_detail
            myform.user = request.user
            myform.save()

    else:
        form = CommentForm()


    context = {'post' : post_detail , 'all_comments' : post_coments , 'form'  : form}

    return render(request , 'post_detail.html' ,context )



def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        form.save()
    else:
        form = PostForm()

    return render(request , 'post_create.html' , {'form' : form})


def post_update(request , id):
    post_detail = Post.objects.get(id=id)

    if request.method == 'POST':
        form = PostForm(request.POST , instance=post_detail)
        form.save()
    else:
        form = PostForm(instance=post_detail)
        
    return render(request , 'update_post.html' , {'form' : form})