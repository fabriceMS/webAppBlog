from django.shortcuts import render, get_object_or_404
from blog.models import Post, PostCategory, Comment
from blog import model_helpers
from blog import navigation

# Create your views here.
# def post_list(request):
#     posts = Post.objects.all()
#     context = {
#         'posts': posts,
#     }
#     return render(request, 'blog/post_list.html', context)


# Default value
def post_list(request, category_name=model_helpers.post_category_all.slug()):
    
    category, posts = model_helpers.get_category_and_posts(category_name)
    categories = model_helpers.get_categories()

    context = {
            'navitation_items': navigation.navigation_items(navigation.NAV_POSTS),
            'posts': posts,
            'category': category,
            'categories': categories,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    posts_same_category = Post.objects.filter(published=True, category = post.category).exclude(pk=post_id)

    # Use the foreign key to get the related comment
    comments = post.comments_FK.exclude(status = Comment.STATUS_HIDDEN).order_by('created_at')


    context = {
            'navitation_items': navigation.navigation_items(navigation.NAV_POSTS),
            'post': post,
            'posts_same_category': posts_same_category,
            'comments': comments

    }
    return render(request, 'blog/post_detail.html', context)


def about(request):
        context = {
               'navitation_items': navigation.navigation_items(navigation.NAV_ABOUT), 
        }
        return render(request, 'blog/about.html', context)