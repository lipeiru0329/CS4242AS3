# Create your views here.
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import ExpertUserForm

def home(request):
    form = ExpertUserForm(request.POST or None)
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        return HttpResponseRedirect('result')
    return render_to_response("search.html",
                              locals(),
                              context_instance=RequestContext(request))

def result(request):
   
    return render_to_response("result.html",
                              locals(),
                              context_instance=RequestContext(request))