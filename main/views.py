import datetime

from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required  
from django.core.exceptions import PermissionDenied        
from django.views.decorators.http import require_POST

from main.forms import ExperienceForm, ProjectForm
from main.models import Experience, Project

# Menampilkan home screen
def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Andranu",
        "full_name": "Andranu Dhawy Purditya",
        "npm": "2506584893",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Second-year CS student at Universitas Indonesia. "
            "Have a deep interest in Artificial Intelligence and Internet of Things."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)

# Menampilkan seluruh projects
def show_project(request):
    is_editor = request.user.groups.filter(name="Editor").exists() == True
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Andranu",
        "title_query": title_query,
        "is_editor": is_editor,
        "form": ProjectForm()
    }
    return render(request, "project.html", context)

# Menambah project
@login_required(login_url="/login/")
def create_project(request):
    if not (request.user.is_superuser or request.user.groups.filter(name="Editor").exists()):
        raise PermissionDenied
    
    form = ProjectForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Proyek baru berhasil ditambahkan!")
        return redirect("main:show_project")

    context = {
        "name": "Andranu",
        "form": form,
    }
    return render(request, "projects_form.html", context)

# Menghapus project
@login_required(login_url="/login/")
def delete_project(request, project_id):
    if not (request.user.is_superuser or request.user.groups.filter(name="Editor").exists()):
        raise PermissionDenied
    
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        project.delete()
        messages.success(request, "Project berhasil dihapus!")
        return redirect("main:show_project")

    return redirect("main:show_project")

def get_projects_json(request):
    title_query = request.GET.get("title", "").strip()
    projects = Project.objects.prefetch_related('starred_by').all()

    if title_query:
        projects = projects.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for project in projects:
        starred_users = project.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "model": "main.project",
            "pk": str(project.id),
            "fields": {
                "title": project.title,
                "description": project.description,
                "thumbnail": project.thumbnail,
                "project_link": project.project_link,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,
            }
        })
    return JsonResponse(data, safe=False)

# Mengedit project
@login_required(login_url="/login/")
def edit_project(request, project_id):
    if not (request.user.is_superuser or request.user.groups.filter(name="Editor").exists()):
        raise PermissionDenied
    project = get_object_or_404(Project, pk=project_id)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, "Project berhasil diupdate!")
            return redirect("main:show_project")
    else:
        form = ProjectForm(instance=project)

    context = {
        "name": "Andranu",
        "form": form,
        "project": project,
    }
    return render(request, "project_edit_form.html", context)

@require_POST
def create_project_ajax(request):
    if not request.user.is_superuser or request.user.groups.filter(name="Editor").exists():
        return JsonResponse(
            {"message": "Hanya pemilik atau editor yang dapat menambahkan proyek."},
            status=403,
        )

    form = ProjectForm(request.POST)
    if form.is_valid():
        project = form.save()
        return JsonResponse(
            {"message": "Proyek berhasil ditambahkan.", "pk": str(project.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)

# Menambah/membuat experience
@login_required(login_url="/login/")
def create_experience(request):
    if not (request.user.is_superuser or request.user.groups.filter(name="Editor").exists()):
        raise PermissionDenied
    form = ExperienceForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Experience baru berhasil ditambahkan!")
        return redirect("main:show_experience")

    context = {
        "name": "Andranu",
        "form": form,
    }
    return render(request, "experiences_form.html", context)

# Menerima experience dalam json
def get_experience_json(request):
    title_query = request.GET.get("title", "").strip()
    experiences = Experience.objects.all()

    if title_query:
        experiences = experiences.filter(title__icontains=title_query)

    data = []
    for experience in experiences:
        data.append({
            "model": "main.experience",
            "pk": str(experience.id),
            "fields": {
                "title": experience.title,
                "description": experience.description,
                "category": experience.category,
                "started_at": experience.started_at,
                "ended_at": experience.ended_at,
                "status": experience.is_ongoing
            }
        })
    return JsonResponse(data, safe=False)

# Menampilkan experience
def show_experience(request):
    is_editor = request.user.groups.filter(name="Editor").exists() == True
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Andranu",
        "title_query": title_query,
        "is_editor": is_editor
    }
    return render(request, "experience.html", context)

# Menghapus experience
@login_required(login_url="/login/")
def delete_experience(request, experience_id):
    if not (request.user.is_superuser or request.user.groups.filter(name="Editor").exists()):
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        experience.delete()
        messages.success(request, "Experience berhasil dihapus!")
        return redirect("main:show_experience")
    return redirect("main:show_experience")

# Mengedit experience
@login_required(login_url="/login/")
def edit_experience(request, experience_id):
    if not (request.user.is_superuser or request.user.groups.filter(name="Editor").exists()):
        raise PermissionDenied
    
    experience = get_object_or_404(Experience, pk=experience_id)

    if request.method == "POST":
        form = ExperienceForm(request.POST, instance=experience)
        if form.is_valid():
            form.save()
            messages.success(request, "Experience berhasil diupdate!")
            return redirect("main:show_experience")
    else:
        form = ExperienceForm(instance=experience)

    context = {
        "name": "Andranu",
        "form": form,
        "experience": experience
    }
    return render(request, "experiences_edit_form.html", context)

# Register account
def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Andranu",
        "form": form,
    }
    return render(request, "register.html", context)

# Login account
def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Andranu",
        "form": form,
    }
    return render(request, "login.html", context)

# Logout account
def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

# Add star
@login_required(login_url="/login/")
def toggle_star(request, project_id):
    project = get_object_or_404(Project, pk=project_id)
    if request.method == "POST":
        if request.user in project.starred_by.all():
            project.starred_by.remove(request.user)
        else:
            project.starred_by.add(request.user)
    return redirect("main:show_project")