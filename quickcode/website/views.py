from django.shortcuts import render
from .models import Problem


def index(request):
    """View function for home page of the site."""
    problems = Problem.objects.all()

    context = {
        'problems': problems
    }

    return render(request, 'index.html', context=context)


def problem(request, problem_id):

    try:

        context = {
            'problem': Problem.objects.get(id=problem_id)
        }

        return render(request, 'problem.html', context=context)

    except Problem.DoesNotExist:
        return render(request, 'not_found.html')



def not_found(request, exception):
    return render(request, 'not_found.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')
