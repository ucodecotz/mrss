from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
# import pandas as pd
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, View
from .models import *
from .forms import *
from django.db.models import Q
from .forms import ProblemForm, AddSolutionForm


class ProblemList(ListView):
    model = Problems
    template_name = 'index.html'
    # context_object_name = ''


class PresentProblem(View):

    def get(self, *args, **kwargs):
        form = ProblemForm()
        context = {
            'form': form
        }
        return render(self.request, 'present_problem.html', context)

    def post(self, *args, **kwargs):
        form = ProblemForm(self.request.POST or None, self.request.FILES or None)

        if form.is_valid():
            print(form)
            slug = slugify(form.cleaned_data.get('title'))
            present_problem = Problems.objects.filter(slug=slug)
            if present_problem.exists():
                # TODO add some functionality
                messages.warning(self.request, ' Sorry already presented, Try another way')
                return redirect('core:presentProblem')
            else:
                device_type = form.cleaned_data.get('device_type')
                device_brand = form.cleaned_data.get('device_brand')
                title = form.cleaned_data.get('title')
                image = form.cleaned_data.get('image')
                problem_desc = form.cleaned_data.get('problem_desc')
                problem = Problems()

                print(problem.device_brand)
                problem.user = self.request.user.userprofile
                problem.title = title
                problem.image = image
                problem.device_brand = device_brand
                problem.device_type = device_type
                problem.problem_desc = problem_desc
                problem.slug = slugify(title)
                problem.save()
                if problem.device_brand == 'T':
                    messages.success(self.request, 'Thanks for presenting your problem to Teckno expert ')
                elif problem.device_brand == 'S':
                    messages.success(self.request, 'Thanks for presenting your problem to Samsung expert ')
                elif problem.device_brand == 'u':
                    messages.success(self.request, 'Thanks for presenting your problem to Huawei expert ')
                elif problem.device_brand == 'I':
                    messages.success(self.request, 'Thanks for presenting your problem to Iphone expert ')
                return redirect('/')
        else:
            print('form not valid')
            messages.warning(self.request, 'Your form was not valid try to fill all field')
            return redirect('core:presentProblem')


class AddSolutionsView(View):
    def get(self, *args, **kwargs):
        form = AddSolutionForm()
        context = {
            'form': form
        }
        return render(self.request, 'add_solution.html', context)


@login_required
def post_solutions(request, pk=None):
    problem = get_object_or_404(Problems, pk=pk)
    if request.method == "POST":
        form = AddSolutionForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            print(form)
            solution_content = form.cleaned_data.get('content')
            solution = Solution()
            solution.problem_id = problem
            solution.content = solution_content
            solution.user = request.user.userprofile
            solution.save()
            messages.success(request, f'Thanks for submitting you solution to {problem.title} ')
            return redirect('core:problem_details', slug=problem.slug)
        else:
            messages.warning(request, 'something went wrong with your form submission')
        return redirect('core:add_solutions', )


class problemDetails(DetailView):
    model = Problems
    template_name = 'problem_details.html'

    def get_context_data(self, **kwargs):
        context = super(problemDetails, self).get_context_data()
        form = AddSolutionForm()
        context.update({
            'form': form
        })
        return context


def post_comments(request, pk):
    solution = get_object_or_404(Solution, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data.get('content')
            new_comment = Comments()
            new_comment.user = request.user.userprofile
            new_comment.solution_id = solution
            new_comment.content = content
            new_comment.save()

            messages.info(request, 'your messages is submitted successfully')

            return redirect('core:problem_details', slug=solution.problem_id.slug)
        else:
            messages.info(request, 'form is invalid')
            return redirect('core:problem_details', slug=solution.problem_id.slug)
    return redirect('core:problem_details', slug=solution.problem_id.slug)


def View_comments(request, pk=None):
    solution = get_object_or_404(Solution, pk=pk)
    comments_qs = Comments.objects.filter(solution_id=solution)
    context = {
        'comment': comments_qs
    }
    return render(request, 'comments.html', context)


# Todo  add models data to tempalate

def blog_post_view(request):
    blog_post_qs = BlogPost.objects.all()
    context = {
        'post_list': blog_post_qs,
    }
    return render(request, 'blog.html', context)


def search_problem(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        problem_submitted = request.GET.get('submit')

        if query is not None:
            lookups = Q(title__icontains=query) | Q(problem_type__icontains=query)

            results = Problems.objects.filter(lookups).distinct()

            context = {'results': results,
                       'submitbutton': problem_submitted}

            return render(request, 'index.html', context)

        else:
            return render(request, 'index.html')

    else:
        return render(request, 'index.html')


class Profile(View):
    def get(self, *args, **kwargs):
        profile = UserProfile.objects.all()
        problem = Problems.objects.all()
        context = {
            'profile': profile,
            'problem': problem
        }
        return render(self.request, 'profile.html', context)
