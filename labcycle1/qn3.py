def Below10k(Bpay):
  DA=Bpay*(5/100)
  HRA=Bpay*(2.5/100)
  MA=500
  PT=20
  PF=Bpay*(8/100)
  GS=Bpay+DA+MA
  D=PT+PF
  salary=GS-D
  print('the gross salary of this customer is ',GS)
  print('the deduction of this customer is ',D)
  print('the net-salary of the customer is ',salary)


def Below30k(Bpay):
  DA=Bpay*(7.5/100)
  HRA=Bpay*(5/100)
  MA=2500
  PT=60
  PF=Bpay*(8/100)
  GS=Bpay+DA+MA
  D=PT+PF
  salary=GS-D
  print('the gross salary of this customer is ',GS)
  print('the deduction of this customer is ',D)
  print('the net-salary of the customer is ',salary)

def Below50k(BPay):
  DA=Bpay*(11/100)
  HRA=Bpay*(7.5/100)
  MA=5000
  PT=60
  PF=Bpay*(11/100)
  IT=Bpay*(11/100)
  GS=Bpay+DA+MA
  D=PT+PF+IT
  salary=GS-D
  print('the gross salary of this customer is ',GS)
  print('the deduction of this customer is ',D)
  print('the net-salary of the customer is ',salary)

def Else(Bpay):
  DA=Bpay*(25/100)
  HRA=Bpay*(11/100)
  MA=7000
  PT=80
  PF=Bpay*(12/100)
  IT=Bpay*(20/100)
  GS=Bpay+DA+MA
  D=PT+PF+IT
  salary=GS-D
  print('the gross salary of this customer is ',GS)
  print('the deduction of this customer is ',D)
  print('the net-salary of the customer is ',salary)



name=input("Enter the customer's name : ")
code=input("Enter the customer's code : ")
Bpay=int(input("Enter the basic pay :"))

if Bpay>1000:
  print('name :',name)
  print('code :',code)
  Below10k(Bpay)

elif Bpay>10000 and Bpay<30000:
  print('name :',name)
  print('code :',code)
  Below30k(Bpay)

elif Bpay>30000 and Bpay<50000:
  print('name :',name)
  print('code :',code)
  Below50k(Bpay)

else:
  print('name :',name)
  print('code :',code)
  Else(Bpay)