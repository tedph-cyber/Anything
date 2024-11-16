from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'blog_anything/index.html')

def section_list(request):
    sections = Section.objects.all()
    return render(request, 'blog_anything/section_list.html', {'sections': sections})

def post_list(request, section_slug):
    section = get_object_or_404(Section, slug=section_slug)
    posts = section.posts.all()
    return render(request, 'blog_anything/post_list.html', {'section': section, 'posts': posts})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('post_list')
    return render(request, 'blog_anything/login.html')

def register_view(request):
    form = UserCreationForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')
    return render(request, 'blog_anything/register.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

def about(request):
    context = {
        'team_members': ['Ted', 'Aardei'],
        'description': 'This is a blog about anything, really!',
    }
    return render(request, 'blog_anything/about.html', context)



def search(request):
    query = request.GET.get('query', '')  # Retrieve the search term from the query string
    results = Section, Post.objects.filter(
        Q(name__icontains=query) | Q(description__icontains=query)  # Adjust fields as needed
    ) if query else []

    context = {
        'results': results,
        'query': query
    }
    return render(request, 'search_results.html', context)