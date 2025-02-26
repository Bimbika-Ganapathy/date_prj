# from django.shortcuts import render

# # Create your views here.
# import datetime
# from django.http import HttpResponse

# def cdt(request):
#     dt=datetime.datetime.now()
  
#     resp = "<h1><body bgcolor='green'> Current Date and Time is %s </body></h1>" % dt


#     return HttpResponse(resp)


from django.shortcuts import render
import datetime
from django.http import HttpResponse

def dynamicdate(request, s):
        t = int(s)
        dt = datetime.datetime.now() + datetime.timedelta(hours=t)

        if t < 0:
            resp = "<h1 style='background-color: yellow;'> Current date and time behind %d hours is %s </h1>" % (abs(t), dt)
        elif t > 0:
            resp = "<h1 style='background-color: blue;'> Current date and time ahead %d hours is %s </h1>" % (t, dt)
        else:
            resp = "<h1 style='background-color: green;'> There is no change in current date and time </h1>"

        return HttpResponse(resp)
   
   
   
    # <html>
    #     <body style="background-color:{bg_color}; text-align:center; color:white;">
    #         <h1>Current Date and Time: {dt}</h1>
    #     </body>
    # </html>
    # """
    
   
