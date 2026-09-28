from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse
from .models import Jogo

class CatalogoTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.usuario = get_user_model().objects.create_user(username='avaliador', password='SenhaDeTeste!482')

    def setUp(self):
        self.jogo = Jogo.objects.get(ordem=1)
        self.dados = {
            'titulo': 'Jogo de teste', 'subtitulo': 'Teste de catálogo',
            'ano': 2020, 'desenvolvedora': 'Estúdio de teste', 'genero': 'Fantasia',
            'ordem': 4, 'sinopse': 'Sinopse de teste.', 'plataformas': 'Windows', 'estrutura': 'Capítulos', 'jogabilidade': 'Explorar e combater.', 'pontos_fortes': 'Narrativa.', 'pontos_fracos': 'Interface.', 'sucesso': 'Análise de teste.', 'aprendizados': 'Melhorar a apresentação.', 'referencias': 'Fonte | https://www.gog.com/en/game/the_witcher',
        }

    def test_trilogia_carregada_pelas_migracoes(self):
        self.assertEqual(list(Jogo.objects.values_list('ano', flat=True)), [2007, 2011, 2015])
        self.assertEqual(Jogo.objects.count(), 3)

    def test_paginas_publicas_e_detalhes(self):
        for nome in ['jogos:home', 'jogos:lista', 'login']:
            self.assertEqual(self.client.get(reverse(nome)).status_code, 200)
        for jogo in Jogo.objects.all():
            self.assertContains(self.client.get(jogo.get_absolute_url()), jogo.titulo)

    def test_visitante_nao_altera_banco(self):
        urls = [reverse('jogos:criar'), reverse('jogos:editar', args=[self.jogo.pk]), reverse('jogos:excluir', args=[self.jogo.pk])]
        for url in urls:
            for metodo in [self.client.get, self.client.post]:
                resposta = metodo(url, self.dados) if metodo == self.client.post else metodo(url)
                self.assertEqual(resposta.status_code, 302)
                self.assertTrue(resposta.url.startswith(reverse('login') + '?next='))
        self.assertEqual(Jogo.objects.count(), 3)
        self.jogo.refresh_from_db()
        self.assertEqual(self.jogo.titulo, 'The Witcher')

    def test_botoes_ocultos_e_visiveis_conforme_login(self):
        for url in [reverse('jogos:lista'), self.jogo.get_absolute_url()]:
            self.assertNotContains(self.client.get(url), reverse('jogos:editar', args=[self.jogo.pk]))
            self.assertNotContains(self.client.get(url), reverse('jogos:excluir', args=[self.jogo.pk]))
        self.client.force_login(self.usuario)
        self.assertContains(self.client.get(reverse('jogos:lista')), reverse('jogos:editar', args=[self.jogo.pk]))
        self.assertContains(self.client.get(self.jogo.get_absolute_url()), reverse('jogos:excluir', args=[self.jogo.pk]))

    def test_login_e_logout_nativos(self):
        resposta = self.client.post(reverse('login'), {'username': 'avaliador', 'password': 'SenhaDeTeste!482'})
        self.assertRedirects(resposta, reverse('jogos:lista'))
        self.assertIn('_auth_user_id', self.client.session)
        self.assertEqual(self.client.get(reverse('logout')).status_code, 405)
        self.assertRedirects(self.client.post(reverse('logout')), reverse('jogos:home'))
        self.assertNotIn('_auth_user_id', self.client.session)

    def test_criar_e_editar_com_modelform(self):
        self.client.force_login(self.usuario)
        self.assertEqual(self.client.get(reverse('jogos:criar')).status_code, 200)
        self.assertEqual(self.client.get(reverse('jogos:editar', args=[self.jogo.pk])).status_code, 200)
        resposta = self.client.post(reverse('jogos:criar'), self.dados)
        jogo = Jogo.objects.get(ordem=4)
        self.assertRedirects(resposta, jogo.get_absolute_url())
        self.dados['titulo'] = 'Título atualizado'
        self.assertRedirects(self.client.post(reverse('jogos:editar', args=[jogo.pk]), self.dados), jogo.get_absolute_url())
        jogo.refresh_from_db()
        self.assertEqual(jogo.titulo, 'Título atualizado')

    def test_formulario_invalido_nao_grava(self):
        self.client.force_login(self.usuario)
        self.dados['ano'] = 1900
        resposta = self.client.post(reverse('jogos:criar'), self.dados)
        self.assertEqual(resposta.status_code, 200)
        self.assertIn('ano', resposta.context['form'].errors)
        self.assertEqual(Jogo.objects.count(), 3)
        self.dados['ano'] = 2020
        self.dados['ordem'] = 1
        resposta = self.client.post(reverse('jogos:criar'), self.dados)
        self.assertIn('ordem', resposta.context['form'].errors)

    def test_excluir_exige_post_e_confirmacao(self):
        self.client.force_login(self.usuario)
        url = reverse('jogos:excluir', args=[self.jogo.pk])
        self.assertContains(self.client.get(url), 'Confirmar exclusão')
        self.assertTrue(Jogo.objects.filter(pk=self.jogo.pk).exists())
        self.assertEqual(self.client.delete(url).status_code, 405)
        self.assertRedirects(self.client.post(url), reverse('jogos:lista'))
        self.assertFalse(Jogo.objects.filter(pk=self.jogo.pk).exists())

    def test_csrf_obrigatorio_nas_mutacoes(self):
        cliente = Client(enforce_csrf_checks=True)
        cliente.force_login(self.usuario)
        for url in [reverse('jogos:criar'), reverse('jogos:editar', args=[self.jogo.pk]), reverse('jogos:excluir', args=[self.jogo.pk])]:
            self.assertEqual(cliente.post(url, self.dados).status_code, 403)
        self.assertEqual(Jogo.objects.count(), 3)

    def test_registro_inexistente_retorna_404(self):
        self.assertEqual(self.client.get(reverse('jogos:detalhe', args=[9999])).status_code, 404)
        self.client.force_login(self.usuario)
        for nome in ['jogos:editar', 'jogos:excluir']:
            self.assertEqual(self.client.get(reverse(nome, args=[9999])).status_code, 404)

    def test_catalogo_vazio(self):
        Jogo.objects.all().delete()
        self.assertContains(self.client.get(reverse('jogos:lista')), 'O catálogo está vazio')

    def test_analises_e_fontes_presentes(self):
        for jogo in Jogo.objects.all():
            jogo.full_clean()
            resposta = self.client.get(jogo.get_absolute_url())
            for titulo in ['Pontos fortes', 'Pontos fracos', 'Por que se destacou', 'Melhorias e aprendizados', 'Fontes e contexto']:
                self.assertContains(resposta, titulo)
            self.assertGreaterEqual(len(jogo.fontes), 3)
            self.assertIn('Inferência editorial:', jogo.aprendizados)

    def test_fontes_rejeitam_protocolo_inseguro(self):
        self.client.force_login(self.usuario)
        self.dados['referencias'] = 'Link inválido | javascript:alert(1)'
        resposta = self.client.post(reverse('jogos:criar'), self.dados)
        self.assertEqual(resposta.status_code, 200)
        self.assertIn('referencias', resposta.context['form'].errors)
        self.assertEqual(Jogo.objects.count(), 3)

    def test_login_preserva_destino(self):
        destino = reverse('jogos:editar', args=[self.jogo.pk])
        resposta = self.client.post(reverse('login'), {'username': 'avaliador', 'password': 'SenhaDeTeste!482', 'next': destino})
        self.assertRedirects(resposta, destino)
