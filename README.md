# Django + Celery + Redis

Este é um exemplo de configuração básica do Celery com Django para agendar tarefas periódicas e tarefas assíncronas.

### Pré-requisitos

Certifique-se de ter os seguintes pacotes instalados:

- Python 3.x
- Django
- Celery
- Redis (como broker para Celery)

Instale as dependências com:

```bash
pip install -r requirements.txt
```

## Configuração do Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis de ambiente:

```plaintext
CELERY_BROKER_REDIS_URL=redis://localhost:6379
DEBUG=True
```

## Configuração do Celery

Certifique-se de ter o Redis instalado e rodando na porta padrão (6379).
Adicione a seguinte configuração ao seu arquivo settings.py:

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers.DatabaseScheduler'

### Utilização

Neste exemplo, temos algumas tarefas de exemplo configuradas:

    multiply_two_numbers: Multiplica dois números e retorna o resultado.
    add: Soma dois números e retorna o resultado.

Você pode agendar essas tarefas no Django admin com base nas configurações definidas no arquivo settings.py.

Para iniciar o Celery, execute o seguinte comando na raiz do projeto Django:

```bash
celery -A cfehome worker --beat --scheduler django --loglevel=info
```
