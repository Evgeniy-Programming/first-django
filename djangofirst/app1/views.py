from django.shortcuts import render
from app1.models import Worker

# Create your views here.

def index_page(request):

    # Worker.objects.get(id=1).delete() - удаляет поле с id = 5
    # переменная.save() - сохранить изменения в БД

    all_workers = Worker.objects.all() # получает все записи из таблицы Worker
    # objects.all - вызывает все строки таблицы
    # Пример: Модель.objects.all() 

    workers_filters = Worker.objects.filter(salary = 60000) # фильтр данных с зп 60к
    # параметры можно указывать через запятую

    # пробежаться по всем данным 
    # for i in Worker.objects.all(): - иная интерпретация
    for i in all_workers:
        print(i.second_name, i.name, i.salary)
    return render(request, 'index.html')
