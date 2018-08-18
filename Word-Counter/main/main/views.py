from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request, 'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    word_dict = {}

    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sorted_words = sorted(word_dict.items(), key = operator.itemgetter(1), reverse= True)

    print(fulltext)
    return render(request, 'count.html', {'fulltext':fulltext, 'count': len(wordlist), 'sorted_words':sorted_words})
