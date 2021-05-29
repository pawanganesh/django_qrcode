from django.apps import AppConfig


class WebsitesConfig(AppConfig):
    name = 'websites'

    def ready(self):
        import websites.signals
