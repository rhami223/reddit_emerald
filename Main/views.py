from django.shortcuts import render
from django.views import View
from Main.models import Subreddit

class indexView(View):
    def get(self, request):
        return render(request, "index.html", {"subreddits": Subreddit.all()})