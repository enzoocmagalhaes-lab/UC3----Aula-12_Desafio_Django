from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from .validators import validar_referencias

class Jogo(models.Model):
    titulo = models.CharField('título', max_length=200)
    subtitulo = models.CharField('frase de apresentação', max_length=160)
    ano = models.PositiveSmallIntegerField('ano do lançamento original', validators=[MinValueValidator(1950), MaxValueValidator(2100)])
    desenvolvedora = models.CharField('desenvolvedora', max_length=150, default='CD PROJEKT RED')
    genero = models.CharField('gênero', max_length=100, default='RPG de fantasia sombria')
    plataformas = models.CharField('plataformas no lançamento original', max_length=200)
    estrutura = models.CharField('estrutura do jogo', max_length=200)
    ordem = models.PositiveSmallIntegerField('ordem na trilogia', unique=True, validators=[MinValueValidator(1)])
    sinopse = models.TextField('história e proposta')
    jogabilidade = models.TextField('como se joga')
    pontos_fortes = models.TextField('pontos fortes')
    pontos_fracos = models.TextField('pontos fracos')
    sucesso = models.TextField('sucesso e resultado comercial')
    aprendizados = models.TextField('melhorias e aprendizados')
    referencias = models.TextField('fontes consultadas', validators=[validar_referencias])

    class Meta:
        ordering = ['ordem', 'ano', 'titulo']
        verbose_name = 'jogo'
        verbose_name_plural = 'jogos'

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('jogos:detalhe', args=[self.pk])

    @property
    def fontes(self):
        fontes = []
        for linha in self.referencias.splitlines():
            nome, separador, url = linha.partition('|')
            # Defesa também na apresentação de registros inseridos fora do formulário.
            if separador and url.strip().startswith(('https://', 'http://')):
                fontes.append({'nome': nome.strip(), 'url': url.strip()})
        return fontes
