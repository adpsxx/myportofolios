from django.shortcuts import render

from main.models import Experience


def show_main(request):
    context = {
        "name": "Andranu",
        "full_name": "Andranu Dhawy Purditya",
        "npm": "2506584893",
        "study_program": "S1 Ilmu Komputer",
        "bio": (
            "Second-year CS student at Universitas Indonesia. "
            "Have a deep interest in Artificial Intelligence and Internet of Things."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Andranu",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)