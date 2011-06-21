# -*- coding: utf-8 -*-

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class Autor(models.Model):
    cod = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=45)
    nacionalidade = models.CharField(max_length=45, blank=True)
    info_bib = models.TextField(blank=True)
    foto = models.ImageField(upload_to='autorfoto', blank=True, null=True) # This field type is a guess.
    class Meta:
        verbose_name_plural = "Autores"
        db_table = u'autor'
        
    def __unicode__(self):
        return self.nome

class Editora(models.Model):
    cnpj = models.IntegerField(primary_key=True, verbose_name='CNPJ')
    razao_social = models.CharField(max_length=45)
    endereco = models.CharField(max_length=90, blank=True)
    class Meta:
        db_table = u'editora'
    def __unicode__(self):
        return self.razao_social

class Publicacao(models.Model):
    cod = models.IntegerField(primary_key=True)
    titulo = models.CharField(max_length=45)
    data_lancamento = models.DateField()
    ano = models.IntegerField()
    estoque = models.IntegerField()
    capa = models.ImageField(upload_to='publicacaocapa', blank=True, null=True) # This field type is a guess.
    resenha = models.TextField(blank=True)
    editora_cnpj = models.ForeignKey(Editora, db_column='editora_cnpj')
    assunto = models.CharField(max_length=45)
    tipo = models.CharField(max_length=45)
    autores = models.ManyToManyField(Autor)
    class Meta:
        verbose_name_plural = u"Publicações"
        db_table = u'publicacao'
    def __unicode__(self):
        return self.titulo

class Imagem(models.Model):
    arquivo = models.ImageField(upload_to='imagens', blank=True, null=True) # This field type is a guess.
    publicacao_cod = models.ForeignKey(Publicacao, db_column='publicacao_cod')
    cod = models.IntegerField(primary_key=True)
    class Meta:
        verbose_name_plural = u"Imagens"
        db_table = u'imagem'
    def __unicode__(self):
        return self.cod

#class PublicacaoHasAutor(models.Model):
#    publicacao_cod = models.ForeignKey(Publicacao, db_column='publicacao_cod')
#    autor_cod = models.ForeignKey(Autor, db_column='autor_cod')
#    class Meta:
#        db_table = u'publicacao_has_autor'

class Venda(models.Model):
    cod = models.IntegerField(primary_key=True)
    data = models.DateField()
    encomenda = models.BooleanField()
    endereco = models.CharField(max_length=45, blank=True)
    publicacoes = models.ManyToManyField(Publicacao)
    class Meta:
        db_table = u'venda'
    def __unicode__(self):
        return self.cod

#class VendaHasPublicacao(models.Model):
#    venda_cod = models.ForeignKey(Venda, db_column='venda_cod')
#    publicacao_cod = models.ForeignKey(Publicacao, db_column='publicacao_cod')
#    qtde = models.IntegerField()
#    valor = models.IntegerField()
#    class Meta:
#        db_table = u'venda_has_publicacao'


