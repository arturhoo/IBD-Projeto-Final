# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Editora(models.Model):
    cnpj = models.IntegerField(primary_key=True)
    razao_social = models.CharField(max_length=45)
    endereco = models.CharField(max_length=90)
    class Meta:
        db_table = u'editora'

class Imagem(models.Model):
    arquivo = models.TextField() # This field type is a guess.
    publicacao_cod = models.ForeignKey(Publicacao, db_column='publicacao_cod')
    cod = models.IntegerField()
    class Meta:
        db_table = u'imagem'

class PublicacaoHasAutor(models.Model):
    publicacao_cod = models.ForeignKey(Publicacao, db_column='publicacao_cod')
    autor_cod = models.ForeignKey(Autor, db_column='autor_cod')
    class Meta:
        db_table = u'publicacao_has_autor'

class Autor(models.Model):
    cod = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    nacionalidade = models.CharField(max_length=45)
    info_bib = models.TextField()
    foto = models.TextField() # This field type is a guess.
    class Meta:
        db_table = u'autor'

class Venda(models.Model):
    cod = models.IntegerField(primary_key=True)
    data = models.DateField()
    encomenda = models.BooleanField()
    endereco = models.CharField(max_length=45)
    class Meta:
        db_table = u'venda'

class VendaHasPublicacao(models.Model):
    venda_cod = models.ForeignKey(Venda, db_column='venda_cod')
    publicacao_cod = models.ForeignKey(Publicacao, db_column='publicacao_cod')
    qtde = models.IntegerField()
    valor = models.IntegerField()
    class Meta:
        db_table = u'venda_has_publicacao'

class Publicacao(models.Model):
    cod = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=45)
    data_lancamento = models.DateField()
    ano = models.IntegerField()
    estoque = models.IntegerField()
    capa = models.TextField() # This field type is a guess.
    resenha = models.TextField()
    editora_cnpj = models.ForeignKey(Editora, db_column='editora_cnpj')
    assunto = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    class Meta:
        db_table = u'publicacao'

