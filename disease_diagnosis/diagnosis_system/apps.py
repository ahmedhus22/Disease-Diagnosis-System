from django.apps import AppConfig


class DiagnosisSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'diagnosis_system'

    def ready(self):
        import diagnosis_system.signals
