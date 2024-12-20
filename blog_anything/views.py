from django.shortcuts import render, get_object_or_404, redirect
from .models import Section, Post
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from .forms import SectionForm, PostForm


# Create your views here.
def home(request):
    sections = Section.objects.all()

    # Attach the latest post to each section
    for section in sections:
        latest_post = section.posts.order_by('-created_at').first()
        section.latest_post = latest_post

    return render(request, "blog_anything/index.html", {'sections': sections})

@login_required
def section_list(request):
    sections = Section.objects.all()
    return render(request, 'blog_anything/section_list.html', {'sections': sections})

@login_required
def post_list(request, section_slug):
    section = get_object_or_404(Section, slug=section_slug)
    posts = section.posts.all()
    return render(request, 'blog_anything/post_list.html', {'section': section, 'posts': posts})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Username: {username}, Password: {password}")
        user = authenticate(request, username=username, password=password)
        print(f"Authenticated User: {user}")
        if user is None:
            messages.error(request, 'Invalid username or password.')
            print("Authentication failed")
        else:  
            login(request, user)
            print("Login successful")
            return redirect('home')  # Redirect to home after successful login
    next_url = request.GET.get('next')
    if next_url:
        messages.error(request, 'You must be logged in to view this page')
    print(messages.get_messages(request))  # This will show you the messages in the console
    return render(request, "blog_anything/login.html")

def post_detail(request, section_slug, post_uuid):
    post = get_object_or_404(Post, uuid=post_uuid)
    section = get_object_or_404(Section, slug=section_slug)
    return render(request, 'blog_anything/post_detail.html', {'post': post})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    next_url = request.GET.get('next')
    if next_url:
        messages.info(request, 'You need to log in to access that page.')
    return render(request, 'blog_anything/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Validation checks and error handling
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists.")
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect after registration
    return render(request, 'blog_anything/register.html')

def logout_view(request):
    logout(request)
    return redirect('home')

def about(request):
    context = {
        'team_members': ['TeD', 'Aardei'],
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

@login_required
def profile_view(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile")
    else:
        form = UserProfileForm(instance=profile)

    return render(request, "blog_anything/profile.html", {"form": form, "profile": profile})

@login_required
def create(request):
    if request.method == 'POST':
        form_1 = SectionForm(request.POST)
        form_2 = PostForm(request.POST)
        if form_1.is_valid() & form_2.is_valid():
            section = form_1.save(commit=False)
            section.created_by = request.user
            section.save()
            post = form_2.save(commit=False)
            post.section = section
            post.created_by = request.user
            post.save()
            return redirect('section_list')
    else:
        form_1 = SectionForm()
        form_2 = PostForm()
    return render(request, 'blog_anything/create.html', {'form_1': form_1, 'form_2': form_2})

@login_required
def post_create(request, section_slug):
    section = get_object_or_404(Section, slug=section_slug)

    if request.method == 'POST':
        # Get the post title from the form
        title = request.POST.get('title')
        
        # Create the post and associate it with the section
        post = Post.objects.create(
            title=title,
            content= request.POST.get('content'),  # Optionally leave content empty or add logic for content later
            section=section,
            created_by=request.user,
        )
        
        messages.success(request, 'Post created successfully.')
        
        
        return redirect('post_list', section_slug=section.slug)
    
    return redirect('home')  # Redirect to home if accessed via GET