from django.apps import AppConfig


class BasketOrderModuleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basket_order_module'
    verbose_name = 'ماژول سبدهای خرید'

    def ready(self):
        import basket_order_module.signals
