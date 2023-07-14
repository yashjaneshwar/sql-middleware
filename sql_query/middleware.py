from django.db import connection
from pygments import highlight
from pygments.formatters import TerminalFormatter
from pygments.lexers import SqlLexer
from sqlparse import format
from django.conf import settings
from decimal import Decimal


class SqlStatsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Call the next middleware or view
        response = self.get_response(request)

        if settings.DEBUG:
            num_queries = len(connection.queries)
            check_duplicates = set()
            total_execution_time = Decimal()
            for query in connection.queries:
                total_execution_time += Decimal(query["time"])
                check_duplicates.add(query["sql"])
                sql_formatted = format(str(query["sql"]), reindent=True)
                print(highlight(sql_formatted, SqlLexer(), TerminalFormatter()))

            print("===========")
            print("[SQL Stats]")
            print(f"{num_queries} Total Queries")
            print(f"{num_queries - len(check_duplicates)} Total Duplicates")
            print(f"{total_execution_time}")
            print("===========")

        return response
