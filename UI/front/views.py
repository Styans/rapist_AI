from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # Указываем путь к HTML файлу в папке templates
def dynamic_page(request, page):
    try:
        # Рендер шаблона с именем, соответствующим параметру `page`
        return render(request, f'{page}.html')
    except TemplateDoesNotExist:
        # Если шаблон не найден, выбросить 404
        raise Http404(f"Страница {page} не найдена.")