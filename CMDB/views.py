from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.http import HttpResponse
# from django.http import Http404
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Question, Choice
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'cmdb/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


# 问题首页
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('cmdb/index.html')
#     context = {'latest_question_list': latest_question_list, }
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'cmdb/index.html', context)


class DetailView(generic.DetailView):
    model = Question
    template_name = 'cmdb/detail.html'


# 详情
# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist!")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'cmdb/detail.html', {'question': question})
#     # return HttpResponse("You're looking at question %s." % question_id)


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'cmdb/results.html'


# 结果
# def results(request, question_id):
#     # response = "You're looking at the results of question %s."
#     # return HttpResponse(response % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'cmdb/results.html', {'question': question})


# 投票
def vote(request, question_id):
    # return HttpResponse("You're voting on question %s." % question_id)
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'cmdb/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('cmdb:results', args=(question.id,)))


@login_required
def index(request):
    # total_idc =Idc.objects.aggregate(Count('idc_name'))
    # idc_num = total_idc["idc_name__count"]
    # total_host = HostList.objects.aggregate(Count('hostname'))
    # host_num = total_host["hostname__count"]
    return render(request, 'cmdb/index.html', locals())


def login(request):
    return render(request, 'cmdb/login.html', locals())


@csrf_exempt
def authin(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
            auth.login(request, user)
            return render(request, 'cmdb/index.html', {'login_user': request.user})
    else:
            return render(request, 'cmdb/login.html', {'login_err': 'Wrong username or password'})
