from django.http import JsonResponse


def index(request):
    languages = [
        'Javascript',
        'Python',
        'Go',
        'Java',
        'Kotlin',
        'PHP',
        'C#',
        'Swift',
    ]

    response = []

    for language in languages:
        response.append({
            'name': language
        })

    return JsonResponse(response, safe=False)