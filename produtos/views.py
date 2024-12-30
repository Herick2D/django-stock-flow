from django.http import JsonResponse
from django.views import View


class TesteView(View):
    def get(self, request):
        return JsonResponse({"message": "API TÁ FUNCIONAL"}, status=200)
