
from functools import wraps
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned, PermissionDenied
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

def handle_exceptions_get_params(message):
    def decorator(view_func):
        @wraps(view_func)
        def wrapper(*args, **kwargs):
            try:
                return view_func(*args, **kwargs)
            except ObjectDoesNotExist :
                return Response({"error": f"{message} no encontrado"}, status=status.HTTP_404_NOT_FOUND)
            except MultipleObjectsReturned :
                return Response({"error": f"Mas de un {message} encontrado."}, status=status.HTTP_400_BAD_REQUEST)
            except PermissionDenied :
                return Response({"error": "Permiso denegado."}, status=status.HTTP_403_FORBIDDEN)
            except ValidationError as e:
                return Response({"error": e.detail}, status=status.HTTP_400_BAD_REQUEST)
            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return wrapper
    return decorator
        