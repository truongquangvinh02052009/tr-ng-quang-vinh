import math
def Tinh(R):
   if R<0:
       print("Ban kinh khong nho hon 0")
       print("Ban nhap khong hop le")
   else:
       CV=2*R*math.pi
       DT=R*R*math.pi
       print("Chu vi la :",CV)
       print("Dien tich la :",DT)
 
print("-------Tinh Chu Vi, Dien Tich Hinh Tron---------")  
r=float(input("Nhap ban kinh hinh tron: "))
Tinh(r)
