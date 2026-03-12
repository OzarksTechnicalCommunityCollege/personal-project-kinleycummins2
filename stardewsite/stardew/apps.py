from django.apps import AppConfig


class StardewConfig(AppConfig):
    name = 'stardew'

    def ready(self):
        import stardew.signals
