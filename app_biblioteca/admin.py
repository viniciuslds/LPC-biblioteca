from django.contrib import admin
from .models import Pessoa, Livro, Emprestimo, Categoria

@admin.register(Pessoa, Livro, Emprestimo, Categoria)
class AgendaAdmin(admin.ModelAdmin):
    pass
