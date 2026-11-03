from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience, Project


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Fundraising Staff UIGTR 2026",
            description="Drove fundraising revenue through merchandise sales while managing real-time inventory and financial records.",
            category="volunteer",
        )

        self.project = Project.objects.create(
            title="Comchat",
            description="Mobile app for chatting with your community created using Flutter framework.",
            thumbnail="https://ik.imagekit.io/hefciv25h/portfolio/placeholder.jpg"
        )
        

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')
        self.assertNotContains(response, self.project.title)
        self.assertContains(response, f'href="{reverse("main:show_project")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Fundraising Staff UIGTR 2026")
        self.assertEqual(self.experience.category, "volunteer")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

        api_response = self.client.get(reverse("main:get_experience_json"))
        self.assertEqual(api_response.status_code, 200)
        experience_data = api_response.json()[0]["fields"]
        self.assertEqual(experience_data["title"], self.experience.title)
        self.assertEqual(experience_data["description"], self.experience.description)

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:get_experience_json"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertFalse(response.json()[0]["fields"]["status"])

    def test_project_model(self):
        self.assertEqual(str(self.project), "Comchat")
        self.assertEqual(self.project.thumbnail, "https://ik.imagekit.io/hefciv25h/portfolio/placeholder.jpg")

    def test_project_page(self):
        response = self.client.get(reverse("main:show_project"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "project.html")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

        api_response = self.client.get(reverse("api:project-list"))
        self.assertEqual(api_response.status_code, 200)
        project_data = api_response.json()[0]
        self.assertEqual(project_data["title"], self.project.title)
        self.assertEqual(project_data["description"], self.project.description)

    def test_empty_project_page(self):
        Project.objects.all().delete()
        response = self.client.get(reverse("api:project-list"))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])