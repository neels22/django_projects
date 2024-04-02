from django.shortcuts import render,HttpResponse


from django.http import JsonResponse
# Create your views here.


from openai import OpenAI
client = OpenAI(api_key="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")




def home(req):
    return render(req,"index.html")



def chatapi(req):

    if req.method== "POST":
        print(req.prompt)
        response = {"this":"that"}


    
    # response = client.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
    #         {
    #         "role": "user",
    #         "content": ""
    #         }
    #     ],
    #     temperature=1,
    #     max_tokens=256,
    #     top_p=1,
    #     frequency_penalty=0,
    #     presence_penalty=0
    # )
    return JsonResponse(response)