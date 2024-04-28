import random
from celery import shared_task

@shared_task
def add(x, y):
    # O Celery reconhece isso como a tarefa `movies.tasks.add`
    # o nome é propositalmente omitido aqui.
    return x + y

@shared_task(name="multiply_two_numbers")
def mul(x, y):
    # O Celery reconhece isso como a tarefa `multiply_two_numbers`
    # O total é o produto de x e y multiplicado por um número aleatório entre 3 e 100.
    total = x * (y * random.randint(3, 100))
    return total

@shared_task(name="sum_list_numbers")
def xsum(numbers):
    # O Celery reconhece isso como a tarefa `sum_list_numbers`
    # A função retorna a soma de todos os números na lista fornecida.
    return sum(numbers)
