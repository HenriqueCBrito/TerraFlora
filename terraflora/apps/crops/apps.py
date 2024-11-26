from django.apps import AppConfig

class CropsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.crops"

    def ready(self):
        import apps.crops.signals