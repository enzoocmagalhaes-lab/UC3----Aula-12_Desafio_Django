from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validar_referencias(value):
    """Uma fonte por linha, no formato nome | URL HTTP(S)."""
    validar_url = URLValidator(schemes=['https', 'http'])
    for numero, linha in enumerate(value.splitlines(), start=1):
        if not linha.strip():
            continue
        nome, separador, url = linha.partition('|')
        if not separador or not nome.strip():
            raise ValidationError(f'Fonte na linha {numero}: use Nome da fonte | https://endereco.')
        try:
            validar_url(url.strip())
        except ValidationError:
            raise ValidationError(f'Fonte na linha {numero}: informe um endereço HTTP ou HTTPS válido.')
