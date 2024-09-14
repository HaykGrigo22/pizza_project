from django.contrib import admin

from main_page.models import Pizzas, Producers, Basket, WishList


class PizzaAdmin(admin.ModelAdmin):
    list_display = ["title", "producer", "price", "rate"]
    list_display_links = ["title", "producer"]
    list_filter = ["producer", "rate", "thick_type"]
    search_fields = ["title", "price"]
    list_editable = ["price", "rate"]
    fieldsets = [
        (
            None,
            {"fields": ("title", )}
        ),
        (
            "Product type",
            {"fields": ("thick_type",)}
         ),
        (
            "Producer info",
            {"fields": ("producer", "price", "rate")}
        ),
        (
            "image",
            {"fields": ("image",)}
        )
    ]

    def get_search_results(self, request, queryset, search_term):
        if search_term.isdigit():
            return queryset.filter(price__gte=search_term), False
        return super().get_search_results(request, queryset, search_term)


admin.site.register(Pizzas, PizzaAdmin)
admin.site.register(Producers)
admin.site.register(Basket)
admin.site.register(WishList)
