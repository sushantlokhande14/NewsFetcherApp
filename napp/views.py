from django.shortcuts import render
import requests
# Create your views here.
def home(request):
	if request.POST.get("src"):
		try :
			src = request.POST.get("src")
			a1= "http://newsapi.org/v2/top-headlines?"
			a2="country=" + src
			a3= "&apiKey="+"0f91886f5f28405ebf9747e06b7b1a3b"
			wa = a1+ a2+a3
			res= requests.get(wa)
			data= res.json()	
			info = data["articles"]
			return render(request , "home.html" , {"info":info ,"src" :src})
		except Exception as e :
			return render(request , "home.html" ,{"info":str(e)})		

	else:
		return render(request , "home.html")
