from django.apps import AppConfig

class DefaultConfig(AppConfig):
    name = 'members'

    def ready(self):
        import members.signals