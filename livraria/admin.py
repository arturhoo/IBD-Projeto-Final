from livraria.models import Autor, Imagem, Editora, Venda, Publicacao
from django.contrib import admin

class ImagemInline(admin.StackedInline):
    model = Imagem
    extra = 3

class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano')
    search_fields = ('titulo', 'autores__nome')
    inlines = [ImagemInline]

admin.site.register(Autor)
admin.site.register(Imagem)
admin.site.register(Publicacao, PublicacaoAdmin)
admin.site.register(Editora)
admin.site.register(Venda)
