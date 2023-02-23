from django.shortcuts import render

# Create your views here.
import openai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')
model_engine = "text-davinci-002"

@csrf_exempt
def chatbot(request):
    if request.method == "POST":
        user_input = request.POST.get("input", "")
        prompt = f"User: {user_input}\nBot:"
        response = openai.Completion.create(engine=model_engine, prompt=prompt, max_tokens=50)
        bot_response = response.choices[0].text.strip()
        return JsonResponse({"response": bot_response})
    else:
        return JsonResponse({"error": "Invalid request method."})
