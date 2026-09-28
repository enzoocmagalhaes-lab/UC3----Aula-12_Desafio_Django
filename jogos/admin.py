from django.contrib import admin
from .models import Jogo

@admin.register(Jogo)
class JogoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'ano', 'desenvolvedora', 'ordem']
    search_fields = ['titulo', 'desenvolvedora']
    list_filter = ['ano', 'genero']
