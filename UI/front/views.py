from django.shortcuts import render
from django.http import JsonResponse


def index(request):
    return render(request, 'index.html')  # Указываем путь к HTML файлу в папке templates
def dynamic_page(request, page):
    try:
        # Рендер шаблона с именем, соответствующим параметру `page`
        return render(request, f'{page}.html')
    except TemplateDoesNotExist:
        # Если шаблон не найден, выбросить 404
        raise Http404(f"Страница {page} не найдена.")
    

    # Пример вопросов
questions = [
    "Как вы обычно реагируете в стрессовой ситуации?",
    "Какие методы релаксации вы используете?",
    "Как часто вы чувствуете усталость в течение дня?",
]

def get_question(request, question_id):
    if 1 <= question_id <= len(questions):
        return JsonResponse({"question": questions[question_id - 1], "total": len(questions), "current": question_id})
    return JsonResponse({"error": "Вопрос не найден"}, status=404)