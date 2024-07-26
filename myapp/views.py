
from ast import Return
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from joblib import load

model = load('./savedModels/model.joblib')

def home(request):
       
       if request.method == 'POST':
            sepal_length = request.POST["sepal_length"]
            sepal_width = request.POST["sepal_width"]
            petal_length = request.POST["petal_length"]
            petal_width = request.POST["petal_width"]

            y_pred = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
            if y_pred[0] == 0:
                  species = "Setosa"
            elif y_pred[0] == 1:
                  species = "Versicolor"
            else:
                 species = "Virginica"
     
            print(y_pred)
        
        
            return render(request, 'myapp/home.html', {'result': species})
       return render(request, 'myapp/home.html')

      

       
       
  

      
           
           
            



      
