from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostCreation
from .models import Profile, Post, Comment, Vote
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import get_user_model

User = get_user_model()

@login_required
def profile(request, profid=None):
    current = get_object_or_404(Profile, user=request.user)
    
    if profid:
        user = get_object_or_404(User, id=profid)
        dif_user = True
    else:
        user = request.user
        dif_user = False
    
    prof = get_object_or_404(Profile, user=user)
    
    is_following = current.is_following(user)
    
    if request.method == "POST":
        if 'follow' in request.POST:
            current.follow(user)
        elif 'unfollow' in request.POST:
            current.unfollow(user)
        return redirect('profile_id', profid=profid if dif_user else None)
    
    context = {
        "prof": prof, 
        'different_user': dif_user, 
        'current': current,
        'is_following': is_following
    }

    return render(request, "prof.html", context)

def editprof(request):
    user = request.user
    prof = get_object_or_404(Profile, user=user)
    if request.method == "POST":
        profpicture = request.FILES.get("profpic")
        username = request.POST.get("username", user.username)
        first_name = request.POST.get("first_name", user.first_name)
        last_name = request.POST.get("last_name", user.last_name)
        email = request.POST.get("email", user.email)

        if profpicture:
            prof.photo = profpicture

        if username:
            username = username

        if first_name:
            user.first_name = first_name

        if last_name:
            user.last_name = last_name
        
        if email:
            user.email = email
        
        user.save()
        prof.save()
        messages.success(request, "Profile updated successfully!")
        return redirect("profile")
    return render(request, "editprof.html")

@login_required
def home(request): 
    comments = Comment.objects.all() 
    prof = Profile.objects.get(user=request.user)
    following = prof.followers.all()
    following_profiles = Profile.objects.filter(user__in=following)
    posts = Post.objects.filter(user__in=following_profiles)
    form = PostCreation()

    if request.method == 'POST':
        if 'submit-post' in request.POST:
            form = PostCreation(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = prof
                post.save()
                return redirect('home')
            else:
                messages.error(request, 'Error found, post not posted')
                return redirect('home')
        elif 'submit-comment' in request.POST:
            comment = request.POST['comment']
            post_id = request.POST.get('submit-comment')
            try:
                post = Post.objects.get(id=post_id)
                upload = Comment(content=comment, post=post, user=request.user)
                upload.save()
                messages.success(request, 'Comment Posted')
            except Post.DoesNotExist:
                messages.error(request, "Post does not exist")

    context = {
        'posts': posts, 
        'comments': comments,
        'form': form,
    }
    
    return render(request, 'root.html', context)

def like(request, postid):
    user = request.user
    post = Post.objects.get(id=postid)

    existing_vote = Vote.objects.filter(post=post, user=user).first()

    if existing_vote:
        if existing_vote.vote == -1 or existing_vote.vote == 0:
            existing_vote.vote = 1
            existing_vote.save()
        elif existing_vote.vote == 1:
            existing_vote.delete()
    else:
        Vote.objects.create(vote=1, user=user, post=post)

    return redirect('home')

def dislike(request, postid):
    user = request.user
    post = Post.objects.get(id=postid)

    existing_vote = Vote.objects.filter(post=post, user=user).first()

    if existing_vote:
        if existing_vote.vote == 1 or existing_vote.vote == 0:
            existing_vote.vote = -1
            existing_vote.save()
        elif existing_vote.vote == -1:
            existing_vote.delete()
    else:
        Vote.objects.create(vote=-1, user=user, post=post)

    return redirect('home')

def moreprofs(request):
    if request.method == 'POST':
        search = request.POST['term']
        posts = Post.objects.filter(
            Q(user__user__username__icontains=search) |
            Q(content__icontains=search)
        )
        profiles = Profile.objects.filter(
            Q(user__username__icontains=search) |
            Q(id__in=posts.values('user_id'))
        )
        ex_profs = profiles.exclude(user=request.user)
    else:
        ex_profs = Profile.objects.exclude(user=request.user)
    
    return render(request, 'moreprofs.html', {'ex_profs': ex_profs})