from django.shortcuts import render

# Create your views here.
def test_view(request):
    text = "HELLO"
    context = {
        'text':text
    }
    return render(request, 'home.html', context)