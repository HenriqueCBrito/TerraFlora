from django.apps import AppConfig

<<<<<<< HEAD

class CropsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "crops"
=======
class CropsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.crops"

    def ready(self):
        import apps.crops.signals
>>>>>>> guilherme_vinicius
