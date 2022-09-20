from django.shortcuts import render, get_object_or_404
from django.http import Http404
from . models import Post


def post_list(request):
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'blog/list.html', context)

# #To display a single post
# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#     except Post.DoesNotExist:
#         raise Http404('No post found')
    
#     context = {'post': post}
#     return render(request, 'blog/detail.html', context)

#Method 2
#To display a single post
def post_detail(request, id):
    post = get_object_or_404(Post, 
                            id=id, 
                            status=Post.Status.PUBLISHED)
    
    context = {'post': post}
    return render(request, 'blog/detail.html', context)
