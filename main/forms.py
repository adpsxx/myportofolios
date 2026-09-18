from django.forms import DateTimeInput, ModelForm, Select, TextInput, Textarea, URLInput

from main.models import Project, Experience;

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = [
            "title",
            "description",
            "thumbnail",
            "project_link",
        ]

        labels = {
            "title": "Nama Proyek",
            "description": "Deskripsi Proyek",
            "thumbnail": "URL Gambar Proyek",
            "project_link": "URL Proyek",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Portfolio Website",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Proyekmu",
                    "rows": 3,
                }
            ),
            "thumbnail": URLInput(
                attrs={
                    "placeholder": "https://ik.imagekit.io/hefciv25h/portfolio/placeholder.jpg",
                }
            ),
            "project_link": URLInput(
                attrs={
                    "placeholder": "https://github.com/adpsxx",
                }
            ),
        }

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        fields = [
            "title",
            "description",
            "category",
            "ended_at",
        ]

        labels = {
            "title": "Nama Experience",
            "description": "Deskripsi Experience",
            "category": "Kategori Experience",
            "ended_at": "Tanggal Selesai Experience",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Experience Title",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Ceritakan Pengalamanmu",
                    "rows": 3,
                }
            ),
            "category": Select(),
            "ended_at": DateTimeInput(
                attrs={
                    "placeholder": "Tanggal selesai",
                }
            ),
        }
