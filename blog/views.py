from django.shortcuts import render, get_object_or_404
from .models import Post, Author

# Create your views here.

def post_list(request):
    # Отримуємо всі пости з бази даних, використовуючи метод all()
    posts = Post.objects.all()

    # Передаємо дані про пости до шаблону за допомогою контексту
    context = {
        'posts': posts
    }

    # Використовуємо функцію render для відображення шаблону blog/post_list.html з переданим контекстом
    return render(request, 'blog/post_list.html', context)

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def posts_by_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    return render(request, 'blog/posts_by_author.html', {'author': author, 'posts': posts})