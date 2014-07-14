from django.shortcuts import render


def index(request):
	return render(request, 'index.html', {})


def feedback(request):
	return render(request, 'feedback.html', {})
