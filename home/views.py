from django.shortcuts import render,HttpResponse
from home.models import contact,qordata
from django.db import connection
from django.core import serializers
from datetime import date,timedelta
import json


def index(request):
    
    
    if request.method == 'POST':
        
        if 'btn3' in request.POST:
            day=int(request.POST.get('days',1))
            targetdate=date.today()-timedelta(days=day)
            with connection.cursor() as cursor:
                cursor.execute("select * from home_qordata where x_axis >= %s", [targetdate])
                records=cursor.fetchall()
            dates=[record[1] for record in records]
            values=[record[2] for record in records]
           
            dates_str=[date.strftime("%Y-%m-%d") for date in dates]
            
            dates_json=json.dumps(dates_str)
            values_json=json.dumps(values)
            context={
                "dates":dates_json,
                "values":values_json
            }
        return render(request,"index.html",context)
  

        if 'btn1' in request.GET:
            with connection.cursor() as cursor:
                cursor.execut("select * from home_qordata4")
                all_suites=cursor.fetchall()
            print(all_suites)

    
    return render(request,"index.html")
   


    







