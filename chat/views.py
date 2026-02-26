import os
import json
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        try:
            body = json.loads(request.body)
            user_message = body.get("message", "").lower()

            # Correct absolute path to data.json
            file_path = os.path.join(settings.BASE_DIR, "chat", "data.json")

            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Simple keyword matching
            for item in data:
                if user_message in item["title"].lower():
                    return JsonResponse({"reply": item["content"]})

            return JsonResponse({"reply": "Sorry, I couldn't find an answer."})

        except Exception as e:
            return JsonResponse({"error": str(e)})

    return JsonResponse({"error": "Invalid request method"})
