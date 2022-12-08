import sys
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,redirect
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
key=b"Sixteen byte key"



sys.path.insert(1,'D:/All_laptop_data/DATA_STURCTURE/Basic_programming_of_ C,C++,python/Django Frame Work/This is now for practice/Forpractices')
from service import views

from service.models import Service

# print(sys.path)
def userform(request):
        return render(request,"index.html")
    
    # ServiceData=Service.objects.all().order_by("-id") # Order a Quary
'''ServiceData=Service.objects.all().order_by("id")#Applying Limiting Quary. -ev iundexes are not allowed.
    data={
        "servicedata":ServiceData
    }'''
    # print(ServiceData)
    # for x in ServiceData:
    #     print(x)
    # fn=usersform()
    # # data={'form':fn}
    # d={}
    # try:
    #     if request.method=="POST":
    #         if request.POST.get('usern1')=="":
    #             return render(request,"userform.html",{'error':True})
    #         passw=int(request.POST.get('pass1'))
    #         user_name=(request.POST.get('usern1'))
           
    #         d={
    #             'passwor':passw,
    #             'user':user_name,
    #             # 'we':rt,
    #             }
    #         # url="/new/?output={}".format(d['user'])
    #         # if d['passwor']==12345:
    #         #     return HttpResponseRedirect('new')
    #         # else:
    #         #     return HttpResponseRedirect('Worng_pass')
    #         # return HttpResponseRedirect(url)
    # except:
    #     pass
    
    # return render(request,"userform.html",data)'''
    
def saveform(request):
    if request.method=="POST":
        passward=request.POST.get('pass1')
        user_name=request.POST.get('usern1')
        cipher=AES.new(key,AES.MODE_CBC)
        # chiphertext=cipher.encrypt()
        pass_in_str=passward
        ciphertext_name=cipher.encrypt(pad(bytes(user_name,'utf-8'),AES.block_size))
        ciphertext_pass=cipher.encrypt(pad(bytes(pass_in_str,'utf-8'),AES.block_size))
        # ciphertext_name=cipher.decrypt(pad())
        # data=Service(passward=ciphertext_pass,user_name=ciphertext_name)
        # data.save()   
        data={
            'ciphertext_name':'ciphertext_name','ciphertext_pass':'ciphertext_pass'
        }
    return render(request,"userform.html",data)
def savedata(request):
    if request.method=="POST":
        passward=request.POST.get('pass1')
        user_name=request.POST.get('usern1')
        cipher=AES.new(key,AES.MODE_CBC)
        print(passward)
        print(user_name)
        # chiphertext=cipher.encrypt()
        pass_in_str=passward
        ciphertext_name=cipher.encrypt(pad(bytes(user_name,'utf-8'),AES.block_size))
        ciphertext_pass=cipher.encrypt(pad(bytes(pass_in_str,'utf-8'),AES.block_size))
        print(ciphertext_name)
        print(ciphertext_pass)
        # ciphertext_name=cipher.decrypt(pad())
        # data=Service(passward=ciphertext_pass,user_name=ciphertext_name)
        # data.save()   
        data={
            'ciphertext_name1':ciphertext_name,'ciphertext_pass1':ciphertext_pass,
        }
    return render(request,"savedata.html",data)
    # return render(request,"savadata.html")

# def new(request):
#     if request.method=="GET":
#         # return HttpResponse(request)
#         output=request.GET.get('output')
#     return HttpResponse(output)
    
    
    
# def w_pass(request):
#     return HttpResponse('Sorry Worng password')
# # def Google(request):
#     return 


# def submitform(request):
#     d={}
#     try:
#         if request.method=="POST":
#             user_name=(request.POST.get('usern1'))#userform se aaya hua data yhan parr liya gya hai.
#             passw=int(request.POST.get('pass1'))
           
#             d={
#                 'passwor':passw,
#                 'user':user_name,
#                 # 'we':rt,
#                 }
#             url="/new/?output={}".format(d['user'])
#             # if d['passwor']==12345:
#             #     return HttpResponseRedirect('new')
#             # else:
#             #     return HttpResponseRedirect('Worng_pass')
#         return HttpResponse(d['user'])
#         # return HttpResponse(d['passwor'],d['user'])  Ye khojen ki 2 ekk sath kese display karaye.
#     except:
#         pass
  
    # return HttpResponse(request)
    

    
