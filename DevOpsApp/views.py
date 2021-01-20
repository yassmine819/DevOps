from django.shortcuts import render, redirect
from DevOpsApp.challs.scripts import *

# Create your views here.
def home(request):
    return render(request, 'Cryptoapp/home.html')
def choix(request):
    choice = str(request.GET.get('Choix d\'algorithme',"cesar"))
    if choice == "cesar":
        return redirect('Ceasar')
    elif choice == "Homophonic":
        return redirect('Homophonic')
    elif choice == "CBC":
        return redirect('CBC')
    elif choice == "Hill":
        return redirect('Hill')
    elif choice == "Vigenere":
        return redirect('Vigenere')
    elif choice == "Vernam":
        return redirect('Vernam')
    elif choice == "Permutation":
        return redirect('Permutation')
    elif choice== "ECB":
        return redirect('ECB')
    elif choice=="CTR":
        return redirect('CTR')
    elif choice=="RC4":
        return redirect('RC4') 
def Ceasar(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/Ceasar.html')
    else:
        but1 = request.POST.get('exampleRadios')
        if but1 == 'encrypte':
            cpt=1
            try:
                text = request.POST['Plaintext']
                shift = int(request.POST['Shift'])
                Ciphertext=encryptcesar(shift,text)
                info=(Ciphertext!='' and cpt==1)
                return render(request, 'Cryptoapp/Ceasar.html', {'Ciphertext':Ciphertext,'info':info})
            except:
                return render(request, 'Cryptoapp/Ceasar.html',{'error': 'Une erreur s\'est produite'})
        else:
            cpt=2
            try:
                text = request.POST['Plaintext']
                shift = int(request.POST['Shift'])
                Ciphertext=decryptcesar(shift,text)
                info1=(Ciphertext!='' and cpt==2)
                return render(request, 'Cryptoapp/Ceasar.html', {'Ciphertext':Ciphertext,'info1':info1})
            except:
                return render(request, 'Cryptoapp/Ceasar.html',{'error': 'Une erreur s\'est produite'})
def Homophonic(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/Homophonic.html')
    but1 = request.POST.get('exampleRadios')
    if but1 == 'encrypte':
        cpt=1
        try:
            text = request.POST['Plaintext']
            Ciphertext=encrypthomo(text)
            info=(Ciphertext!='' and cpt==1)
            return render(request, 'Cryptoapp/Homophonic.html', {'Ciphertext':Ciphertext,'info':info})
        except:
            return render(request, 'Cryptoapp/Homophonic.html',{'error': 'Une erreur s\'est produite'})
    else:
        cpt=2
        try:
            text = request.POST['Plaintext']
            Ciphertext=decrypthomo(text)
            info1=(Ciphertext!='' and cpt==2)
            return render(request, 'Cryptoapp/Homophonic.html', {'Ciphertext':Ciphertext,'info1':info1})
        except:
            return render(request, 'Cryptoapp/Homophonic.html',{'error': 'Une erreur s\'est produite'})
def CBC(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/CBC.html')
    else:
        but1 = request.POST.get('exampleRadios')
        if but1 == 'encrypte':
            cpt=1
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                Ciphertext=CBCencryption( text,key)
                info=(Ciphertext!='' and cpt==1)
                return render(request, 'Cryptoapp/CBC.html', {'Ciphertext':Ciphertext,'info':info})
            except:
                return render(request, 'Cryptoapp/CBC.html',{'error': 'Une erreur s\'est produite'})
        else:
            cpt=1
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                Ciphertext=CBCdecryption(text,key)
                info=(Ciphertext!='' and cpt==1)
                return render(request, 'Cryptoapp/CBC.html', {'Ciphertext':Ciphertext,'info':info})
            except:
                return render(request, 'Cryptoapp/CBC.html',{'error': 'Une erreur s\'est produite'})
def Hill(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/Hill.html')
    but1 = request.POST.get('exampleRadios')
    if but1 == 'encrypte':
        cpt=1
        try:
            text = request.POST['Plaintext']
            key= request.POST['key']
            print("hey")
            Ciphertext=hillencrypte(text,key)
            print(Ciphertext)
            info=(Ciphertext!='' and cpt==1)
            return render(request, 'Cryptoapp/Hill.html', {'Ciphertext':Ciphertext,'info':info})
        except:
            return render(request, 'Cryptoapp/Hill.html',{'error': 'Une erreur s\'est produite'})
    else:
        cpt=2
        try:
            text = request.POST['Plaintext']
            key= request.POST['key']
            Ciphertext=hilldecrypte(text,key)
            info1=(Ciphertext!='' and cpt==2)
            return render(request, 'Cryptoapp/Hill.html', {'Ciphertext':Ciphertext,'info1':info1})
        except:
            return render(request, 'Cryptoapp/Hill.html',{'error': 'Une erreur s\'est produite'})

def Vigenere(request):
    if request.method == 'GET':    
        return render(request, 'Cryptoapp/Vigenere.html')
    but1 = request.POST.get('exampleRadios')
    if but1 == 'encrypte':
        cpt=1
        try:
            text = request.POST['Plaintext']
            key= request.POST['Key']
            Ciphertext=vignere(text, key, typ='e')
            info=(Ciphertext!='' and cpt==1)
            return render(request, 'Cryptoapp/Vigenere.html', {'Ciphertext':Ciphertext,'info':info})
        except:
            return render(request, 'Cryptoapp/Vigenere.html',{'error': 'Une erreur s\'est produite'})
    else:
        cpt=2
        try:
            text = request.POST['Plaintext']
            key= request.POST['Key']
            Ciphertext=vignere(text, key, typ='d')
            info1=(Ciphertext!='' and cpt==2)
            return render(request, 'Cryptoapp/Vigenere.html', {'Ciphertext':Ciphertext,'info1':info1})
        except:
            return render(request, 'Cryptoapp/Vigenere.html',{'error': 'Une erreur s\'est produite'})
def Vernam(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/Vernam.html')
    but1 = request.POST.get('exampleRadios')
    if but1 == 'encrypte':
        cpt=1
        try:
            text = request.POST['Plaintext']
            key= request.POST['Key']
            Ciphertext=vernamencrypt(key,text)
            info=(Ciphertext!='' and cpt==1)
            return render(request, 'Cryptoapp/Vernam.html', {'Ciphertext':Ciphertext,'info':info})
        except:
            return render(request, 'Cryptoapp/Vernam.html',{'error': 'Une erreur s\'est produite'})
    else:
        cpt=2
        try:
            text = request.POST['Plaintext']
            key= request.POST['Key']
            Ciphertext=vernamdecrypt(key,text)
            info1=(Ciphertext!='' and cpt==2)
            return render(request, 'Cryptoapp/Vernam.html', {'Ciphertext':Ciphertext,'info1':info1})
        except:
            return render(request, 'Cryptoapp/Vernam.html',{'error': 'Une erreur s\'est produite'})
    
def Permutation(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/Permutation.html')
    but1 = request.POST.get('exampleRadios')
    if but1 == 'encrypte':
        cpt=1
        try:
            text = request.POST['Plaintext']
            key= request.POST['Key']
            Ciphertext=encryptSub(key,text)
            infoV=(Ciphertext!='' and cpt==1 and Ciphertext!="")
            return render(request, 'Cryptoapp/Permutation.html', {'Ciphertext':Ciphertext,'info':infoV})
        except:
            return render(request, 'Cryptoapp/Permutation.html',{'error': 'Une erreur s\'est produite'})
    else:
        cpt=2
        try:
            text = request.POST['Plaintext']
            key= request.POST['Key']
            Ciphertext=decryptSub(key,text)
            info1=(Ciphertext!='' and cpt==2)
            return render(request, 'Cryptoapp/Permutation.html', {'Ciphertext':Ciphertext,'info1':info1})
        except:
            return render(request, 'Cryptoapp/Permutation.html',{'error': 'Une erreur s\'est produite'})

def ECB(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/ECB.html')
    else:
        but1 = request.POST.get('exampleRadios')
        if but1 == 'encrypte':
            cpt=1
            try:
                text = request.POST['Plaintext']
                shift = int(request.POST['Shift'])
                key= request.POST['Key']
                Ciphertext=ECBencypt(key,shift,text)
                info=(Ciphertext!='' and cpt==1)
                return render(request, 'Cryptoapp/ECB.html', {'Ciphertext':Ciphertext,'info':info})
            except:
                return render(request, 'Cryptoapp/ECB.html',{'error': 'Une erreur s\'est produite'})
        else:
            cpt=2
            try:
                text = request.POST['Plaintext']
                shift = int(request.POST['Shift'])
                key= request.POST['Key']
                Ciphertext=ECBdecypt(key,shift,text)
                info1=(Ciphertext!='' and cpt==2)
                return render(request, 'Cryptoapp/ECB.html', {'Ciphertext':Ciphertext,'info1':info1})
            except:
                return render(request, 'Cryptoapp/ECB.html',{'error': 'Une erreur s\'est produite'})

def CTR(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/CTR.html')
    else:
        but1 = request.POST.get('exampleRadios')
        if but1 == 'encrypte':
            cpt=1
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                counter = int(request.POST['Counter'])
                Ciphertext=en_dec_CTR(text, key, counter)
                info=(Ciphertext!='' and cpt==1)
                return render(request, 'Cryptoapp/CTR.html', {'Ciphertext':Ciphertext,'info':info})
            except:
                return render(request, 'Cryptoapp/CTR.html',{'error': 'Une erreur s\'est produite'})
        else:
            cpt=2
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                counter = int(request.POST['Counter'])
                Ciphertext=en_dec_CTR(text, key, counter)
                info1=(Ciphertext!='' and cpt==2)
                return render(request, 'Cryptoapp/CTR.html', {'Ciphertext':Ciphertext,'info1':info1})
            except:
                return render(request, 'Cryptoapp/CTR.html',{'error': 'Une erreur s\'est produite'})

def RC4(request):
    if request.method == 'GET':
        return render(request, 'Cryptoapp/RC4.html')
    else:
        but1 = request.POST.get('exampleRadios')
        if but1 == 'encrypte1':
            cpt=1
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                Ciphertext=encrypt_Hex(key, text)
                info=(Ciphertext!='' and cpt==1)
                return render(request, 'Cryptoapp/RC4.html', {'Ciphertext':Ciphertext,'info':info})
            except:
                return render(request, 'Cryptoapp/RC4.html',{'error': 'Une erreur s\'est produite'})
        elif but1 == 'encrypte2':
            cpt=1
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                Ciphertext=encrypt_bin(key, text)
                info=(Ciphertext!='' and cpt==1)
                return render(request, 'Cryptoapp/RC4.html', {'Ciphertext':Ciphertext,'info':info})
            except:
                return render(request, 'Cryptoapp/RC4.html',{'error': 'Une erreur s\'est produite'})
        elif but1 == 'decrypte1':
            cpt=2
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                Ciphertext= decrypt_Hex(key, text)
                info1=(Ciphertext!='' and cpt==2)
                return render(request, 'Cryptoapp/RC4.html', {'Ciphertext':Ciphertext,'info1':info1})
            except:
                return render(request, 'Cryptoapp/RC4.html',{'error': 'Une erreur s\'est produite'})
        else:
            cpt=2
            try:
                text = request.POST['Plaintext']
                key=request.POST['Key']
                Ciphertext= decrypt_bin(key, text)
                info1=(Ciphertext!='' and cpt==2)
                return render(request, 'Cryptoapp/RC4.html', {'Ciphertext':Ciphertext,'info1':info1})
            except:
                return render(request, 'Cryptoapp/RC4.html',{'error': 'Une erreur s\'est produite'})