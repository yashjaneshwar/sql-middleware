from django.shortcuts import render
from .models import Product
import json
from django.http import JsonResponse
from django.core.serializers import serialize
from django.db import connection
# from pprint import pprint
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format


def home(request):
    qs = Product.objects.all()
    serialized_data = serialize('json', qs) # serialize qs into json
    # print(connection.queries)
    q = list(connection.queries)

    for qs in q:
        sqlformatted = format(str(qs["sql"]), reindent = True)
        # print(sqlformatted)
        print(highlight(sqlformatted, SqlLexer(), TerminalFormatter()))

    # loads method is used to pass the valid json string & convert it into python dictonary
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data,safe=False, status = 200)
