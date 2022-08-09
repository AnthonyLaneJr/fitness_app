from django.views.generic import TemplateView


class StartPageView(TemplateView):
    template_name = "pages/start.html"

class HelpPageView(TemplateView):
    template_name = "pages/help_page.html"

class NutritionPageView(TemplateView):
    template_name = "pages/nutritional.html"

class RegistrationPageView(TemplateView):
    template_name = "registration/register.html"