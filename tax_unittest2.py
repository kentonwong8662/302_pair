import unittest
import sys



def tax_calculation(self_income,couple_income):
    print("Salaries Tax Computation")
    #self_income = float(input("Please Self income (per MONTH) :"))
    #couple_income = float(input("Please Spouse income (per MONTH):"))
    print(self_income)
    print(couple_income)

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

    return(separate_tax,couple_separate_tax,joint_separate_tax,)
class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(tax_calculation(10000, 50000), (0, 58500, 55440), "shouldbe 0, 58500, 55440")
    def test2(self):
        self.assertEqual(tax_calculation(50000, 10000), (58500, 0, 55440), "shouldbe 58500, 0, 55440")   
    def test3(self):
        self.assertEqual(tax_calculation(10000, 10000), (0, 0, 0), "shouldbe 0, 0, 0")
    def test4(self):
        self.assertEqual(tax_calculation(20000, 20000), (3760, 3760, 14880), "shouldbe 3760, 3760, 14880")
    def test5(self):
        self.assertEqual(tax_calculation(30000, 30000), (17700, 17700, 53400), "shouldbe 17700, 17700, 53400")
    def test6(self):
        self.assertEqual(tax_calculation(40000, 40000), (38100, 38100, 94200), "shouldbe 38100, 38100, 94200")
    def test7(self):
        self.assertEqual(tax_calculation(50000, 50000), (58500.0, 58500.0, 135000.0), "shouldbe 58500.0, 58500.0, 135000.0")
    def test8(self):
        self.assertEqual(tax_calculation(25000, 25000), (9420.0, 9420.0, 34020.0), "shouldbe 9420, 9420, 34020")
    def test9(self):
        self.assertEqual(tax_calculation(27000, 27000), (12612.0, 12612.0, 41772.0), "shouldbe 12612, 12612, 41772")
       
    def test10(self):
        self.assertEqual(tax_calculation(15964.91, 0), (999.9994799999997, 0, 0), "shouldbe 15964.91, 0, 0")
    def test11(self):
        self.assertEqual(tax_calculation(15964.91, 15964.91), (999.9994799999997, 999.9994799999997, 3999.9968799999983), "shouldbe 999.9994799999997.91, 999.9994799999997, 3999.9968799999983")
    def test12(self):
        self.assertEqual(tax_calculation(15964.91, 15965), (999.9994799999997, 1000.06, 4000.0973999999987), "shouldbe 999.9994799999997.91, 1000.06, 4000.0973999999987")
   
    
    def test13(self):
        self.assertEqual(tax_calculation(15965, 15965), (1000.06, 1000.06, 4000.2), "shouldbe 1000.06, 1000.06, 4000.2")
    def test14(self):
        self.assertEqual(tax_calculation(15964, 15964), (999.7920000000001,999.7920000000001, 3998.751999999997), "shouldbe 999.7920000000001, 999.7920000000001, 3998.751999999997")
    def test15(self):
        self.assertEqual(tax_calculation(20350, 20350), (3999.4,3999.4, 15997.2), "shouldbe 3999.4, 3999.4, 15997.2")
    def test16(self):
        self.assertEqual(tax_calculation(20351, 20351), (4000.1399999999994,4000.1399999999994, 16000.476000000008), "shouldbe 4000.1399999999994, 4000.1399999999994, 16000.476000000008")
    def test17(self):
        self.assertEqual(tax_calculation(24736, 24736), (8999.040000000003,8999.040000000003, 32996.736000000004), "shouldbe 8999.040000000003, 8999.040000000003, 32996.736000000004")
    def test18(self):
        self.assertEqual(tax_calculation(24737, 24737), (9000.251999999999,9000.251999999999, 33000.612000000016), "shouldbe 9000.251999999999, 9000.251999999999, 33000.612000000016")
    def test19(self):
        self.assertEqual(tax_calculation(29122, 29122), (15998.712,15998.712, 49996.87200000002), "shouldbe 15998.712, 15998.712, 49996.87200000002")
    def test20(self):
        self.assertEqual(tax_calculation(29123, 29123), (16000.374000000002,16000.374000000002, 50000.747999999985), "shouldbe 16000.374000000002, 16000.374000000002, 50000.747999999985")
   
        
        
if __name__ == '__main__':
    sys.exit(tax_calculation(0,0))

