import os
from celery import Celery
from celery.schedules import crontab

# Define o módulo de configurações Django padrão para o programa 'celery'.
# Isso também é usado em manage.py
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cfehome.settings')

app = Celery('cfehome')

# Usar uma string aqui significa que o worker não precisa serializar
# o objeto de configuração para processos filhos.
# - namespace='CELERY' significa que todas as chaves de configuração relacionadas ao celery
#   devem ter um prefixo `CELERY_`.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Carrega módulos de tarefas de todas as configurações de aplicativos Django registrados.
app.autodiscover_tasks()

# Usamos CELERY_BROKER_URL em settings.py em vez de:
# app.conf.broker_url = ''

# Usamos CELERY_BEAT_SCHEDULER em settings.py em vez de:
# app.conf.beat_scheduler = ''django_celery_beat.schedulers.DatabaseScheduler'

# Abaixo é para fins ilustrativos. Nós
# configuramos para que possamos ajustar a programação
# no Django admin para gerenciar todas
# Tarefas Periódicas como abaixo
app.conf.beat_schedule = {
    'multiply-task-crontab': {
        'task': 'multiply_two_numbers',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
    'multiply-every-5-seconds': {
        'task': 'multiply_two_numbers',
        'schedule': 5.0,
        'args': (16, 16)
    },
    'add-every-30-seconds': {
        'task': 'movies.tasks.add',
        'schedule': 30.0,
        'args': (16, 16)
    },
}
