from functools import wraps
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

def handle_exceptions_get(message):
    def decorators(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            try:
                return view_func(*args, **kwargs)
            except ObjectDoesNotExist :
                return Response({"error": f"No se encontraron {message}."}, status=status.HTTP_404_NOT_FOUND)
            except ValidationError as e:
                return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return wrapper
    return decorators