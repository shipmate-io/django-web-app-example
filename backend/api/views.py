from django.http import JsonResponse
from django.templatetags.static import static

def index(request):
    languages = [
        'Javascript',
        'Python',
        'Go',
        'Ruby',
        'PHP',
    ]

    response = []

    for language in languages:
        response.append({
            'name': language,
            'logo': request.build_absolute_uri(static(language.lower() + '.svg'))
        })

    return JsonResponse(response, safe=False)