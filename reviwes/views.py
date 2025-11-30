from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from . forms import review_form
from . models import Reviewtable
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormView, CreateView

# Create your views here.

class ReviewView(CreateView):
    model = Reviewtable
    form_class = review_form
    template_name = "reviwes/index.html"
    success_url = "/thank-page"
    
    
    
class ThankYou(TemplateView):
    template_name = "reviwes/thanks.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"]  = "Finished!"
        return context

class ListReviews(ListView):
    template_name ="reviwes/listreviews.html"
    model = Reviewtable
    context_object_name = "reviews"

class SingleReviews(DetailView):
    template_name ="reviwes/singlereviews.html"
    model = Reviewtable
    context_object_name = "review"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        loaded_id = self.object.id
        Liked_id = self.request.session.get("Liked_id")
        context["Is_liked"] = str(loaded_id) == Liked_id
        return context

class AddLikeView(View):
    def post(self, request):
        Liked_id = request.POST["Liked_id"]
        request.session["Liked_id"] = Liked_id
        return HttpResponseRedirect("/list-reviews/" + Liked_id)