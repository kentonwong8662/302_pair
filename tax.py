
print("Salaries Tax Computation")
self_income = float(input("Please Self income (per MONTH) :"))
couple_income = float(input("Please Spouse income (per MONTH):"))
#print(self_income)
#print(couple_income)

#print(married_status)


#madatory contribution
MPF=0
if self_income <7100:
    MPF = 0
elif self_income <=30000:
    MPF = self_income*0.05
else:
    MPF=1500
print('')
print('Self MPF mandatory (per MONTH): $'+str(MPF))
print('Self MPF mandatory (per YEAR): $'+str(MPF*12))


couple_MPF=0
if couple_income <7100:
    couple_MPF = 0
elif couple_income <=30000:
    couple_MPF = couple_income*0.05
else:
    couple_MPF=1500
print('')
print('Spouse MPF mandatory (per MONTH): $'+str(couple_MPF))
print('Spouse MPF mandatory (per YEAR): $'+str(couple_MPF*12))



#Net Chargeable income 
net_chargeable= 0
print('')
print('Self income (per YEAR): $'+str(self_income*12))
#print('')
#print('Allowances (Separate) 20/21: $132000')
#print('')
net_chargeable= (self_income*12) - (MPF*12) - 132000
if net_chargeable<0:
    print('Self Net Chargeable Income: $0')
    net_chargeable=0
else:   
    print('Self Net Chargeable Income: $'+str(net_chargeable))


couple_net_chargeable= 0
print('')
print('Spouse income (per YEAR): $'+str(couple_income*12))
#print('')
#print('Allowances (Separate) 20/21: $132000')
#print('')
couple_net_chargeable= (couple_income*12) - (couple_MPF*12) - 132000
if couple_net_chargeable<0:
    print('Spouse Net Chargeable Income: $0')
    couple_net_chargeable=0
else:   
    print('Spouse Net Chargeable Income: $'+str(couple_net_chargeable))

joint_net_chargeable= 0

#print('')
#print('Allowances (Separate) 20/21: $132000')
#print('')
joint_net_chargeable= (couple_income*12) + (self_income*12) - (couple_MPF*12) - (MPF*12) - 264000
if joint_net_chargeable<0:
    #print('joint Net Chargeable Income: $0')
    joint_net_chargeable=0
else:   
    #print('joint Net Chargeable Income: $'+str(joint_net_chargeable))
    pass

#Salary Tax paid (Separate)
separate_tax=0
if net_chargeable <=50000:
    separate_tax= net_chargeable*0.02
elif net_chargeable <= 100000:
    separate_tax= 1000 + (net_chargeable-50000)*0.06
elif net_chargeable <= 150000:
    separate_tax= 1000 + 3000 +(net_chargeable-100000)*0.1
elif net_chargeable <= 200000:
    separate_tax= 1000 + 3000 + 5000 + (net_chargeable-150000)*0.14
else:
    separate_tax= 1000 + 3000 + 5000 + 7000+ (net_chargeable-200000)*0.17
print('')   
print('Self Tax paid (separate assessment): $'+str(separate_tax))

couple_separate_tax=0
if couple_net_chargeable <=50000:
    couple_separate_tax= couple_net_chargeable*0.02
elif couple_net_chargeable <= 100000:
    couple_separate_tax= 1000 + (couple_net_chargeable-50000)*0.06
elif couple_net_chargeable <= 150000:
    couple_separate_tax= 1000 + 3000 +(couple_net_chargeable-100000)*0.1
elif couple_net_chargeable <= 200000:
    couple_separate_tax= 1000 + 3000 + 5000 + (couple_net_chargeable-150000)*0.14
else:
    couple_separate_tax= 1000 + 3000 + 5000 + 7000+ (couple_net_chargeable-200000)*0.17
#print('')   
print('Spouse Tax paid (separate assessment): $'+str(couple_separate_tax))
print('Total Tax paid (separate assessment): $'+str(couple_separate_tax+separate_tax))

joint_separate_tax=0
if joint_net_chargeable <=50000:
    joint_separate_tax= joint_net_chargeable*0.02
elif joint_net_chargeable <= 100000:
    joint_separate_tax= 1000 + (joint_net_chargeable-50000)*0.06
elif joint_net_chargeable <= 150000:
    joint_separate_tax= 1000 + 3000 +(joint_net_chargeable-100000)*0.1
elif joint_net_chargeable <= 200000:
    joint_separate_tax= 1000 + 3000 + 5000 + (joint_net_chargeable-150000)*0.14
else:
    joint_separate_tax= 1000 + 3000 + 5000 + 7000+ (joint_net_chargeable-200000)*0.17
print('')   

print('Total Tax paid (joint assessment): $'+str(joint_separate_tax))

if (couple_separate_tax+separate_tax) > joint_separate_tax:
    print('')   
    print('')   
    print("You should choose JOINT assessment")

elif (couple_separate_tax+separate_tax) < joint_separate_tax:
    print('')   
    print('')   
    print("You should choose SEPERATE assessment")

else:
    print("You should choose either assessment")




