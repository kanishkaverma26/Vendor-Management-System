from django.apps import AppConfig


class VendorManagementConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_app'

    def ready(self):
        import vendor_app.signals
