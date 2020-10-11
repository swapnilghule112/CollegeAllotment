from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import UploadForm
from .models import UserData
from  django.views.decorators.csrf import csrf_exempt
import pandas as pd
import random
import os

@csrf_exempt
def create_profile(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            user_sheet = form.save(commit=False)
            user_sheet.student_data = request.FILES['student_data']
            file_type = user_sheet.student_data.url.split('.')[-1]
            file_type = file_type.lower()
            user_sheet.save()
            file_name = user_sheet.student_data
            df = pd.read_csv(file_name)

            # DEPARTMENTS = ["CMPN", "INFT", "EXTC", "ETRX", "BIOMED"]
            # list1,list2,list3,list4,list5 = [],[],[],[],[]
            # for i in range(1,1001):
            #     random.shuffle(DEPARTMENTS)
            #     list1.append(DEPARTMENTS[0])
            #     list2.append(DEPARTMENTS[1])
            #     list3.append(DEPARTMENTS[2])
            #     list4.append(DEPARTMENTS[3])
            #     list5.append(DEPARTMENTS[4])
            # df["Pref1"] = list1
            # df["Pref2"] = list2
            # df["Pref3"] = list3
            # df["Pref4"] = list4
            # df["Pref5"] = list5

            df1 = df.sort_values(["CET","M","P","C","PCM","Aggr"],ascending=False)

            count = {
            "CMPN": user_sheet.CMPN,
            "INFT": user_sheet.INFT,
            "EXTC": user_sheet.EXTC,
            "ETRX": user_sheet.ETRX,
            "BIOMED": user_sheet.BIOMED,
            }
            allotment = []
            for i in df1.itertuples():
                if count[i.Pref1] != 0:
                    count[i.Pref1] -= 1
                    allotment.append(i.Pref1)
                elif count[i.Pref2] != 0:
                    count[i.Pref2] -= 1
                    allotment.append(i.Pref2)
                elif count[i.Pref3] != 0:
                    count[i.Pref3] -= 1
                    allotment.append(i.Pref3)
                elif count[i.Pref4] != 0:
                    count[i.Pref4] -= 1
                    allotment.append(i.Pref4)
                elif count[i.Pref5] != 0:
                    count[i.Pref5] -= 1
                    allotment.append(i.Pref5)
                else:
                    allotment.append("NOT Alloted")
            df1["allotment"] = allotment

            list_id	= df1["id"]
            list_first_name = df1["first_name"]	
            list_email = df1["email"]
            list_CET = df1["CET"]
            list_M = df1["M"]
            list_P = df1["P"]
            list_C = df1["C"]
            list_PCM = df1["PCM"]
            list_Aggr = df1["Aggr"]
            list_Pref1 = df1["Pref1"]
            list_Pref2 = df1["Pref2"]
            list_Pref3 = df1["Pref3"]
            list_Pref4 = df1["Pref4"]
            list_Pref5 = df1["Pref5"]
            list_allotment = df1["allotment"]

            files = {
                "list_id": list_id,
                "list_first_name": list_first_name,
                "list_email": list_email,
                "list_CET": list_CET,
                "list_M": list_M,
                "list_P": list_P,
                "list_C": list_C,
                "list_PCM": list_PCM,
                "list_Aggr": list_Aggr,
                "list_Pref1": list_Pref1,
                "list_Pref2": list_Pref2,
                "list_Pref3": list_Pref3,
                "list_Pref4": list_Pref4,
                "list_Pref5": list_Pref5,
                "list_allotment": list_allotment
            }
            x = []
            y = []
            context = zip(
                list_id,
                list_first_name,
                list_email,
                list_CET,
                list_M,
                list_P,
                list_C,
                list_PCM,
                list_Aggr,
                list_Pref1,
                list_Pref2,
                list_Pref3,
                list_Pref4,
                list_Pref5,
                list_allotment,
            )

            excel_file = df1.to_csv("media/alloted.csv")
            # content = open('media/alloted.csv').read()
            # response = HttpResponse(content, content_type='text/plain')
            # response['Content-Length'] = os.path.getsize('media/alloted.csv')
            # response['Content-Disposition'] = 'attachment; filename=%s' % 'alloted.csv'
            # return response
            return render(request, 'CollegeAllotmentApp/result.html', {'context':context})
    context = {"form": form,}
    return render(request, 'CollegeAllotmentApp/home.html', context)


def download_report(request):
    if request.method == "POST":
        content = open('media/alloted.csv').read()
        response = HttpResponse(content, content_type='text/plain')
        response['Content-Length'] = os.path.getsize('media/alloted.csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % 'alloted.csv'
        return response
    else:
        return redirect('home')