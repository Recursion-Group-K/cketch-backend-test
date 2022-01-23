from django.contrib import admin
from .models import Drawing


@admin.register(Drawing)
class Drawing(admin.ModelAdmin):
    pass
