from .submission_logic import test_submission
from django.shortcuts import render
from .models import Problem, TestCase, Submission
from .forms import SubmissionForm


def index(request):
    """View function for home page of the site."""
    problems = Problem.objects.all()

    context = {
        'problems': problems
    }

    return render(request, 'index.html', context=context)


def problem(request, problem_id):
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if not form.is_valid():
            print(form.errors)
            return render(request, 'not_found.html')
        else:
            submission = Submission(file=form.cleaned_data['file'], problem=Problem.objects.get(id=problem_id),
                                    language=form.cleaned_data['language'])
            submission.save()

            test_submission(submission, problem_id)

    try:
        context = {
            'problem': Problem.objects.get(id=problem_id),
            'submissions': Submission.objects.filter(problem_id=problem_id),
            'form': SubmissionForm()
        }
        return render(request, 'problem.html', context=context)

    except (Submission.DoesNotExist, Problem.DoesNotExist):
        return render(request, 'not_found.html')


def not_found(request, exception):
    return render(request, 'not_found.html')


def login(request):
    return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')
