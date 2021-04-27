class Atm(object):
    def __init__(self,pin_number,creditcardnumber):
        self.pin_number = pin_number
        self.creditcardnumber = creditcardnumber
        
        
    def cashWithdrawl(self):
        print('cash withdrawn')
    def  BalanceEnquiry(self):
        print(' BalanceEnquiry')

    def accelerate(self):
        print('accelerate')
    def change_gear(self,gear_type):
        print('gearchanged')
RBI = Atm('0000','12-34-56')
print(RBI.cashWithdrawl())
print(RBI.BalanceEnquiry())