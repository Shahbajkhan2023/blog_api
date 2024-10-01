from .models import Post


def global_context(request):

    user_profile = None
    if request.user.is_authenticated:
        user_profile = request.user.profile

    recent_posts = Post.objects.order_by('-created_at')[:5]

    return {
        'user_profile': user_profile,
        'recent_profile': recent_posts,
    }
