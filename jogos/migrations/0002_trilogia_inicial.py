from django.db import migrations

JOGOS = [{'titulo': 'The Witcher',
  'subtitulo': 'A estreia que definiu a identidade do Lobo Branco.',
  'ano': 2007,
  'ordem': 1,
  'plataformas': 'Windows',
  'estrutura': 'Capítulos com áreas interligadas',
  'sinopse': 'Geralt de Rívia, um caçador de monstros conhecido como bruxo, retorna sem suas memórias e se '
             'envolve na investigação de um ataque a Kaer Morhen. A busca pelos responsáveis o leva a '
             'Vizima, onde crime, preconceito e disputas entre facções tornam difícil separar monstros de '
             'pessoas. A aventura se passa no universo literário criado por Andrzej Sapkowski e apresenta '
             'uma continuação própria para os jogos.',
  'jogabilidade': 'O jogador explora áreas organizadas em capítulos, conversa com personagens e decide como '
                  'resolver conflitos. O combate utiliza cliques no momento certo para encadear ataques, '
                  'alternando estilos conforme o inimigo. Preparar poções, estudar criaturas e escolher '
                  'equipamentos ajuda a transformar a investigação em vantagem nas batalhas.',
  'pontos_fortes': 'Identidade marcante: a ambientação sombria e os conflitos sociais dão personalidade ao '
                   'mundo, evitando uma divisão simples entre heróis e vilões.\n'
                   '\n'
                   'Escolhas difíceis: decisões podem produzir consequências posteriores, tornando a '
                   'neutralidade uma posição complicada.\n'
                   '\n'
                   'Preparação relevante: alquimia e estilos de combate reforçam o papel de Geralt como '
                   'especialista que precisa conhecer suas presas.',
  'pontos_fracos': 'Combate peculiar: o ritmo de cliques pode parecer distante e repetitivo para quem espera '
                   'controle de ação direto. É uma diferença de proposta, mas também uma barreira de '
                   'entrada.\n'
                   '\n'
                   'Acabamento irregular na estreia: carregamentos demorados e problemas de localização em '
                   'inglês prejudicavam a fluidez e a compreensão. A Enhanced Edition corrigiu parte '
                   'importante dessas limitações.\n'
                   '\n'
                   'Apresentação envelhecida: animações e interface têm menos naturalidade do que nos jogos '
                   'seguintes.',
  'sucesso': 'Marco histórico: em outubro de 2008, a CD Projekt anunciou 1 milhão de cópias vendidas, '
             'somando o jogo original e a Enhanced Edition; o anúncio foi noticiado pela GameSpot. O número '
             'não representa apenas a edição de 2007 nem as vendas atuais.\n'
             '\n'
             'Análise editorial: o diferencial foi oferecer uma fantasia adulta com dilemas persistentes e '
             'uma identidade própria. Esse resultado deu à estreia espaço para construir uma comunidade, '
             'mesmo com suas limitações técnicas. Não há base para atribuir as vendas a uma única '
             'característica.',
  'aprendizados': 'Melhoria documentada: a descrição oficial da Enhanced Edition registra revisão de '
                  'diálogos em inglês, organização melhor do inventário, maior estabilidade e redução dos '
                  'tempos de carregamento.\n'
                  '\n'
                  'Inferência editorial: a resposta mostra a importância de apresentar bem uma boa história. '
                  'Localização, interface e desempenho não são detalhes separados da narrativa; eles '
                  'determinam se o jogador consegue acompanhá-la. Essa é uma interpretação das mudanças, não '
                  'uma declaração literal da empresa.',
  'referencias': 'GOG — descrição e melhorias da Enhanced Edition | https://www.gog.com/en/game/the_witcher\n'
                 'GameSpot — crítica da Enhanced Edition (2008) | '
                 'https://www.gamespot.com/reviews/the-witcher-enhanced-edition-review/1900-6198321/\n'
                 'GameSpot — marco de 1 milhão de cópias (30/10/2008) | '
                 'https://www.gamespot.com/articles/the-witcher-enchants-1-million/1100-6200343/',
  'desenvolvedora': 'CD PROJEKT RED',
  'genero': 'RPG de fantasia sombria'},
 {'titulo': 'The Witcher 2: Assassins of Kings',
  'subtitulo': 'A política assume o centro, e as escolhas mudam o caminho.',
  'ano': 2011,
  'ordem': 2,
  'plataformas': 'Windows',
  'estrutura': 'Capítulos com grandes ramificações narrativas',
  'sinopse': 'Acusado de envolvimento no assassinato de um rei, Geralt precisa investigar uma conspiração '
             'enquanto os Reinos do Norte se aproximam de uma crise. Sua busca atravessa alianças militares, '
             'conflitos entre humanos e não humanos e interesses que raramente são transparentes. O foco se '
             'desloca da investigação local para as consequências políticas de cada decisão.',
  'jogabilidade': 'O combate passa a privilegiar ação direta, com ataques, esquivas, sinais mágicos e '
                  'preparação. A exploração ocorre em regiões delimitadas, não em um mundo aberto contínuo. '
                  'Uma decisão importante ao fim do primeiro ato muda profundamente o segundo: aliados, '
                  'lugares e acontecimentos variam, oferecendo motivos concretos para jogar novamente.',
  'pontos_fortes': 'Ramificações expressivas: as escolhas alteram partes substanciais da campanha, em vez de '
                   'mudar somente uma fala ou o encerramento.\n'
                   '\n'
                   'Intriga envolvente: personagens com interesses conflitantes tornam difícil encontrar uma '
                   'solução moralmente confortável.\n'
                   '\n'
                   'Salto de apresentação: cenários detalhados, diálogos e encenação tornam a aventura mais '
                   'cinematográfica sem abandonar o foco nas decisões.',
  'pontos_fracos': 'Entrada exigente: o lançamento foi criticado por combates iniciais difíceis e situações '
                   'frustrantes antes que o jogador dominasse os sistemas.\n'
                   '\n'
                   'Usabilidade irregular: inventário, comparação de equipamentos e alguns problemas em '
                   'missões interrompiam o fluxo.\n'
                   '\n'
                   'Contexto e encerramento: a densidade política exige atenção, e o trecho final pode '
                   'parecer mais abrupto do que os atos anteriores. Conhecer os nomes e facções faz '
                   'diferença.',
  'sucesso': 'Marco histórico: em outubro de 2013, a CD Projekt informou 6 milhões de cópias vendidas dos '
             'dois primeiros jogos somados. Esse total é da série naquele momento; não deve ser apresentado '
             'como venda individual de The Witcher 2.\n'
             '\n'
             'Análise editorial: a sequência consolidou a proposta de um RPG em que decisões mudam a '
             'experiência. A combinação de produção mais sofisticada com caminhos alternativos sustentou seu '
             'destaque crítico e o interesse pela continuação. O dado conjunto mostra crescimento da '
             'franquia, mas não permite isolar quanto cada fator contribuiu.',
  'aprendizados': 'Melhoria documentada: a versão 2.0 acrescentou um tutorial mais completo; a Enhanced '
                  'Edition incorporou esse tutorial e outros aprimoramentos, além de conteúdo narrativo '
                  'adicional. Essas mudanças são descritas na página oficial do produto na GOG.\n'
                  '\n'
                  'Inferência editorial: profundidade e dificuldade funcionam melhor quando o jogador '
                  'entende as regras. Ensinar os sistemas com clareza preserva o desafio, enquanto uma '
                  'apresentação insuficiente pode transformar aprendizado em frustração. As ramificações '
                  'também mostram o valor de dar consequências perceptíveis às escolhas.',
  'referencias': 'GameSpot — crítica do lançamento (2011) | '
                 'https://www.gamespot.com/reviews/the-witcher-2-assassins-of-kings-review/1900-6314759/\n'
                 'GOG — tutorial e melhorias da Enhanced Edition | '
                 'https://www.gog.com/en/game/the_witcher_2\n'
                 'CD Projekt — 6 milhões nos dois primeiros jogos (2013) | '
                 'https://www.cdprojekt.com/en/media/news/6-million-witchers-in-6-years/',
  'desenvolvedora': 'CD PROJEKT RED',
  'genero': 'RPG de fantasia sombria'},
 {'titulo': 'The Witcher 3: Wild Hunt',
  'subtitulo': 'O mundo cresce, mas as histórias pessoais continuam no centro.',
  'ano': 2015,
  'ordem': 3,
  'plataformas': 'Windows, PlayStation 4 e Xbox One',
  'estrutura': 'Mundo aberto dividido em grandes regiões',
  'sinopse': 'Em uma terra devastada pela guerra, Geralt procura Ciri, sua filha de criação, perseguida pela '
             'Caçada Selvagem. A busca atravessa povoados, cidades e ilhas, aproximando conflitos íntimos de '
             'disputas capazes de afetar reinos inteiros. Relações familiares, lealdade e responsabilidade '
             'dão um centro emocional à escala da aventura.',
  'jogabilidade': 'O jogador percorre regiões abertas, aceita contratos de monstros, investiga pistas e '
                  'participa de histórias secundárias. Espadas, esquivas, sinais e alquimia compõem o '
                  'combate. As escolhas nos diálogos afetam personagens e desfechos, enquanto atividades '
                  'como Gwent criam pausas entre viagens e confrontos.',
  'pontos_fortes': 'Missões com peso humano: histórias secundárias apresentam conflitos próprios e '
                   'incentivam a curiosidade, em vez de depender apenas de recompensas.\n'
                   '\n'
                   'Mundo com personalidade: direção de arte e ambientação dão identidade às regiões e às '
                   'pessoas que vivem nelas.\n'
                   '\n'
                   'Escala com vínculo emocional: a busca por Ciri conecta o mundo aberto a relações que '
                   'importam para Geralt e para o jogador.',
  'pontos_fracos': 'Movimentação e câmera: a crítica de lançamento apontou respostas pesadas e dificuldades '
                   'de seleção de alvos em confrontos movimentados.\n'
                   '\n'
                   'Inventário trabalhoso: o volume de itens podia dificultar a organização na versão '
                   'inicial.\n'
                   '\n'
                   'Investigação pouco exigente: seguir pistas realçadas nem sempre pede dedução do jogador. '
                   'Certos deslocamentos entre personagens também alongam o ritmo. Esses pontos variam de '
                   'importância conforme a preferência de quem joga; não anulam o valor das histórias.',
  'sucesso': 'Marco histórico: a CD Projekt informou 6 milhões de cópias vendidas nas primeiras seis semanas '
             'após o lançamento de 2015. O comunicado também descreveu uma distribuição internacional ampla '
             'e o plano de suporte prolongado. Esse é um resultado inicial, não o total atual.\n'
             '\n'
             'Análise editorial: combinar exploração, personagens memoráveis e missões com consequências '
             'ajudou o jogo a se destacar. A chegada simultânea a PC e consoles ampliou seu alcance. '
             'Qualidade, distribuição e continuidade do suporte compõem uma explicação plausível; o anúncio '
             'de vendas não mede isoladamente o efeito de cada uma.',
  'aprendizados': 'Princípios documentados: na GDC 2023, Paweł Sasko apresentou lições de design apoiadas em '
                  'The Witcher 3 e Cyberpunk 2077. A cobertura da palestra destaca clareza na entrega de '
                  'informação, consequências visíveis para as escolhas e redução de complexidade que não '
                  'melhora a experiência. São lições de uma trajetória com vários projetos, não apenas deste '
                  'jogo.\n'
                  '\n'
                  'Inferência editorial: um mapa maior precisa preservar a qualidade dos encontros e das '
                  'decisões. A escala tem valor quando oferece histórias significativas; adicionar tarefas '
                  'ou sistemas sem propósito pode diluir justamente o que diferencia a série.',
  'referencias': 'PC Gamer — crítica da versão de lançamento (2015) | '
                 'https://www.pcgamer.com/the-witcher-3-review/\n'
                 'CD Projekt — 6 milhões nas primeiras seis semanas (2015) | '
                 'https://www.cdprojekt.com/en/media/news/the-cd-projekt-group-summarizes-the-release-of-the-witcher-3/\n'
                 'GDC — palestra de Paweł Sasko sobre design de missões (2023) | '
                 'https://www.gdcvault.com/play/1028897/10-Key-Quest-Design-Lessons\n'
                 'Game Developer — síntese das lições da palestra (2023) | '
                 'https://www.gamedeveloper.com/marketing/10-key-takeaways-from-the-quest-design-of-cyberpunk-2077-and-the-witcher-3',
  'desenvolvedora': 'CD PROJEKT RED',
  'genero': 'RPG de fantasia sombria'}]

def cadastrar_trilogia(apps, schema_editor):
    Jogo = apps.get_model('jogos', 'Jogo')
    for dados in JOGOS:
        Jogo.objects.using(schema_editor.connection.alias).create(**dados)

class Migration(migrations.Migration):
    dependencies = [('jogos', '0001_initial')]
    operations = [migrations.RunPython(cadastrar_trilogia, migrations.RunPython.noop)]
