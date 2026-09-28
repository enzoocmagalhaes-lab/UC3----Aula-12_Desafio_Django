from django import forms
from .models import Jogo

class JogoForm(forms.ModelForm):
    class Meta:
        model = Jogo
        fields = ['titulo', 'subtitulo', 'ano', 'desenvolvedora', 'genero', 'plataformas', 'estrutura', 'ordem', 'sinopse', 'jogabilidade', 'pontos_fortes', 'pontos_fracos', 'sucesso', 'aprendizados', 'referencias']
        widgets = {nome: forms.Textarea(attrs={'rows': 4}) for nome in ['sinopse', 'jogabilidade', 'pontos_fortes', 'pontos_fracos', 'sucesso', 'aprendizados', 'referencias']}
        help_texts = {
            'ordem': 'Escolha um número ainda não usado no catálogo.',
            'pontos_fortes': 'Separe os aspectos em parágrafos.',
            'pontos_fracos': 'Indique a edição ou época quando a crítica depender da versão.',
            'sucesso': 'Date números de vendas e diferencie fatos de interpretação.',
            'aprendizados': 'Diferencie melhorias documentadas de sua análise.',
            'referencias': 'Uma fonte por linha: Nome da fonte | https://endereco',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
