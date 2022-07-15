from calendar import c
import os
from secrets import choice
import pandas as pd
import time

dictionary = {}
myCSV = 'Student.csv'

clear = lambda: os.system('clear')


def add_note():
  clear()
  global dictionary
  names=input("Öğrencinin ismi:")
  no=input("Öğrencinin numarası:")
  mid=input("Vize notu:")
  final=input("Final notu:")
  avg = calculate_avarage(int(mid),int(final))
  ltr=calculate_letter(avg)
  sts="Geçti" if avg>=50 else "Kaldı"
  message=f"{names} {no}; Vize Notu: {mid}, Final Notu: {final}, Ortalama: {avg}, Harf Notu: {ltr}, Durumu: {sts}"
  dictionary = {"Adı":[names],"Numarası":[no],"Vize":[mid],"Final":[final],"Ortalama":[avg],"Harf":[ltr],"Durum":[sts]}
  class_note = pd.DataFrame(dictionary)
  if(os.path.exists(myCSV) and os.path.isfile(myCSV)):
    class_note.to_csv('Student.csv', mode='a', index=False, header=False)
  else:
    class_note.to_csv('Student.csv', mode='a', index=False)
    
  print(message)
  print("Not kaydedildi anasayfaya dönüş yapılıyor")
  time.sleep(3)
  clear()
  return 0

def calculate_avarage(mid,final):
  if 0<=mid<=100 and 0<=final<=100:
    return(mid*0.4)+(final*0.6)
  else:
    print("Girilen notlar hatalıdır. Uygulama kapatılıyor")
    time.sleep(2)
    exit()

def calculate_letter(avarage):
  if 90<=avarage:
    return "AA"
  elif 85<=avarage:
    return "BA"
  elif 80<=avarage:
    return "BB"
  elif 75<=avarage:
    return "CB"
  elif 70<=avarage:
    return "CC"
  elif 60<=avarage:
    return "DC"
  elif 50<=avarage:
    return "DD"
  elif 40<=avarage:
    return "FD"
  elif 0<=avarage:
    return "FF"

def show_class():
  clear()
  student = pd.read_csv('Student.csv')
  print(student)
  exitFnc = 1
  while exitFnc!=0:
    print("Çıkmak için 0 yazınız")
    exitFnc=int(input())
    if exitFnc == 0:
        print("Ana Sayfaya dönüş yapılıyor")
        time.sleep(3)
        clear()
        return 0

def clear_note():
    clear()
    if(os.path.exists(myCSV) and os.path.isfile(myCSV)):
        print("Dosyayı silmekte eminmisiniz? y/n")
        chc=input()
        if chc=="y":
            os.remove(myCSV)
            print("Dosya Silindi")
            print("Anasayfaya dönüş yapılıyor")
            time.sleep(1.5)
            return 0
        else:
            print("Dosya silinmedi")
            print("Anasayfaya dönüş yapılıyor")
            time.sleep(1.5)
            clear()
            return 0
    else:
        print("Olmayan Dosyayı Silemezsiniz")
        print("Anasayfaya dönüş yapılıyor")
        time.sleep(1.5)
        clear()
        return 0

choice = 1
print("-----Not Sistemine Hoşgeldiniz-----")
while choice!=0: 
    print("Lütfen Seçiminizi Belirtiniz:")
    print("1) Not ekleme")
    print("2) Sınıfın Durumu")
    print("3) Sınıfın Verilerini Sil")
    print("0) Çıkış")
    choice = int(input("Seçiminiz: "))
    if choice==1:
        add_note()
    elif choice==2:
        show_class()
    elif choice==3:
        clear_note()
    elif choice==0:
        print("Çıkış yapılıyor")
        time.sleep(1.5)
    else:
        print("Hatalı seçim lütfen belirtilen sayılardan başka sayı seçmeyiniz")
        time.sleep(3)
        clear()
        
    