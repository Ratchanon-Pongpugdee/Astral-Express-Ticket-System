# -*- coding: utf-8 -*-
"""
Created: 2023-09-?? 14:36
Updated: 2026-09-21 20:00   

@author: group4
"""

# ***** class Moneyset and Stationset *****
class Moneyset:
    """(2026-09-05) 
        class for Money Set:
        for Wallet File, wlMem, cashIn, changeBox
    """
    def __init__(self,mCode="",mName="",mValue=0,mQty=0,mAmt=0):
        """(2026-09-05)
            a special method used to initialize a newly created object
            Constructor to create new object 
        """
        self.mCode  = mCode
        self.mName  = mName
        self.mValue = mValue
        self.mQty   = mQty
        self.mAmt   = mAmt

    def __str__(self):
        """(2026-09-05)
            a special method used to covert object to string(Text)
            Printing method to convert object to text for print()
        """
        return f'{self.mCode:6}{self.mName:16}{self.mValue:8d}{self.mQty:6d}{self.mAmt:10d}'

    def showTotalAmount(self):
        """(2026-09-05) 
            a custom method for show mValue*mQty
        """
        return (self.mValue*self.mQty)

    def showAllMoneyData(self):
        """(2026-09-05) 
            a custom method for show All Money Data 
        """
        return f'{self.mCode}, {self.mName}, {self.mValue}, {self.mQty}, {self.mAmt}'

class Stationset:
    """(2026-09-05) 
        class for Station Set:
        for Station File, wlMem, cashIn, changeBox
    """
    
    def __init__(self,sCode="",sName="",sPrice=0,pIN=0,pOUT=0):
        """(2024-08-28) Constructor Method to create Stationset instance """
        """(2026-09-05)
            a special method used to initialize a newly created object
            Constructor to create new object 
        """
        self.sCode  = sCode
        self.sName  = sName
        self.sPrice = sPrice
        self.pIN    = pIN
        self.pOUT   = pOUT

    def __str__(self):
        """(2026-09-05)
            a special method used to covert object to string(Text)
            Printing method to convert object to text for print()
        """
        return f'{self.sCode:6}{self.sName:20}{self.sPrice:8d}{self.pIN:10d}{self.pOUT:10d}'

    def showAllStationData(self):
        return f'{self.sCode}, {self.sName}, {self.sPrice}, {self.pIN}, {self.pOUT}'

    def showAllStationDataShort(self):
        return f'{self.sCode:6}{self.sName:20}{self.sPrice:8d}'


# ***** Read File To Memory *****
def loadWalletData(walletFN):
    """(2026-09-05) 
        อ่าน Wallet.txt แล้วสร้าง Moneyset เก็บลง moneyMem 
    """
    
    fin = open(walletFN, 'r')

    mnMem = []
    l = 0
    with fin:
        for mnRec in fin:
            mCode, mName, mValue, mQty, mAmt = mnRec.split()
            if l:
                mValue = int(mValue)
                mQty = int(mQty)
                mAmt = mValue*mQty
                mnMem.append(Moneyset(mCode, mName, mValue, mQty, mAmt))          
            else:
                mnCol = f'{mCode:6}{mName:16}{mValue:>8}{mQty:>6}{mAmt:>10}'

            l += 1

    return mnCol, mnMem

def loadStationData(stationFN):
    """(2024-09-22) 
        อ่าน Station File stMem โดยสร้าง Stationset แต่ละรายการ
    """
    fin = open(stationFN, 'r')
   
    stMem = []
    l = 0
    with fin:
        for stRec in fin:
            fields = stRec.split()
            sCode = fields[0]
            sName = ' '.join(fields[1:-3])
            sPrice, pIN, pOUT = fields[-3:]
            if l:
                sPrice  = int(sPrice)
                pIN     = int(pIN)
                pOUT    = int(pOUT)
                stMem.append(Stationset(sCode, sName, sPrice, pIN, pOUT))          
            else:
                stCol = f'{sCode:6}{sName:20}{sPrice:>8}{pIN:>10}{pOUT:>10}'

            l += 1

    return stCol, stMem


# ***** Show All Memory *****
def showAllMoneyMem(mnCol, mnMem):
    """(2026-09-05) 
        แสดง Money Memory ทั้งหมด พร้อมรวม mAmt ทั้งหมด
    """
    
    sumAmt = 0
    print(mnCol)
    
    for mnRec in mnMem:
        sumAmt += mnRec.mAmt
        print(mnRec)
        
    return sumAmt

def calculateWalletTotal(mnMem):
    """(2026-09-05) 
        รวมยอด mAmt ของเงินทุกชนิด 
    """
    
    sumAmt = 0
    
    for mnRec in mnMem:
        sumAmt += mnRec.mAmt
        
    return sumAmt

def showAllStationData(stCol, stMem):
    """(2024-09-22) 
        แสดงสถานีทั้งหมด พร้อมรวม pIN และ pOUT
    """
    
    sumIN  = 0
    sumOUT = 0
    print(stCol)
    
    for stRec in stMem:
        sumIN  += stRec.pIN
        sumOUT += stRec.pOUT
        print(stRec)
        
    return sumIN, sumOUT

def showStationList(stCol, stMem):
    """(2024-09-22) 
        แสดงข้อมูลสถานีแบบสั้น และยังรวม pIN / pOUT ด้วย
    """
    
    sumIN  = 0
    sumOUT = 0
    print(stCol)

    for stRec in stMem:
        sumIN  += stRec.pIN
        sumOUT += stRec.pOUT
        print(stRec.showAllStationDataShort())
        
        
    return sumIN, sumOUT


# ***** Write Memory to File *****
def saveWalletData(mnCol, mnMem, wlFN):
    """(2024-09-22) 
        เอา Money Memory เขียนกลับไปที่ไฟล์ Wallet.txt 
    """

    fout = open(wlFN, 'w')

    with fout:       
        fout.write(mnCol +'\n')
        for mnRec in mnMem:
            newRec = mnRec.__str__()
            fout.write(f'{newRec}\n')

    return

def saveStationData(stCol, stMem, stFN):
    """(2024-09-22) 
        เอา Station Memory เขียนกลับไปที่ไฟล์ Stations.txt 
    """

    fout = open(stFN, 'w')

    with fout:       
        fout.write(stCol +'\n')
        for stRec in stMem:
            newRec = stRec.__str__()
            fout.write( f'{newRec}\n')

    return


# ***** money and stations memory, clear, copy, add  *****     
def clearWalletQuantity(mMem, clrQty=0):
    """(2026-09-05) 
        สร้าง Money Memory ชุดใหม่ โดยกำหนดจำนวนmQty เป็นค่าที่กำหนดโดยเริ่มdefault เป็น 0 
    """
    newMem = []
    for mRec in mMem:
        mAmt = mRec.mValue * clrQty 
        mNew = Moneyset(mRec.mCode,mRec.mName,mRec.mValue,clrQty,mAmt)
        newMem.append(mNew)

    return newMem

def copyWalletData(mMem):
    """(2026-09-05) 
        Copy Money Memory ไปสร้างชุดใหม่ 
    """

    newMem = []
    for mRec in mMem:
        mAmt = mRec.mValue * mRec.mQty
        mNew = Moneyset(mRec.mCode,mRec.mName,mRec.mValue,mRec.mQty,mAmt)
        newMem.append(mNew)

    return newMem

def combineWalletData(maMem, mbMem):
    """(2026-09-05) 
        เอา Money Memory สองชุดมารวมกัน โดยตรวจว่า code/name/value ตรงกันไหม แล้วรวม mQty 
        errcode ==  0(False)     is not error
        errcode !=  0(True)      is error    
    """
    
    errcode = 0
    alen = len(maMem)
    blen = len(mbMem)

    newMem = []    
    if alen == blen:
        for i in range(alen):
            if (maMem[i].mCode == mbMem[i].mCode) and \
               (maMem[i].mName == mbMem[i].mName) and \
               (maMem[i].mValue == mbMem[i].mValue) :
                   abQty = maMem[i].mQty + mbMem[i].mQty
                   abAmt = maMem[i].mValue * abQty
                   mNew = Moneyset(maMem[i].mCode,maMem[i].mName,maMem[i].mValue,abQty,abAmt)
                   newMem.append(mNew)
            else:
                errcode = i+1
                break
             
    elif alen < blen:
        errcode = blen - alen
        for mRec in mbMem:
            mNew = Moneyset(mRec.mCode,mRec.mName,mRec.mValue,0,0)
            newMem.append(mNew)    
    else:    
        errcode = alen - blen
        for mRec in maMem:
            mNew = Moneyset(mRec.mCode,mRec.mName,mRec.mValue,0,0)
            newMem.append(mNew)    

    return errcode, newMem

def clearPassengerCounts(stMem):
    """(2024-09-21) 
        สร้าง Station Memory ใหม่โดยล้าง pIN และ pOUT เป็น 0 
    """
    newMem = []
    for stRec in stMem:
        stNew = Stationset(stRec.sCode,stRec.sName,stRec.sPrice,0,0)
        newMem.append(stNew)
        
    return newMem

def copyStationData(stMem):
    """(2024-09-21) 
        Copy Station Memory ไปยังชุดใหม่ 
    """
    newMem = []
    for stRec in stMem:
        stNew = Stationset(stRec.sCode,stRec.sName,stRec.sPrice,stRec.pIN,stRec.pOUT)
        newMem.append(stNew)
        
    return newMem

# ***** Maintenance Memory wlMem and stMem ***** 
def updateWalletData(wlMem):
    """(2024-09-22)
        แก้ไข Wallet ทั้งชุด (มีตัวเลือกล้าง mQty ก่อน และคำนวณmAmt ใหม่) 
    """
    clrQty_Flag = input("Clear Qty <y,Y> = ")
    if clrQty_Flag in {'y','Y'}:
        nMem = clearWalletQuantity(wlMem)
    else:
        nMem = copyWalletData(wlMem)

    newMem = []
    editFlag = 0
    for mRec in nMem:
        print(f'\n[{mRec.showAllMoneyData()}]')
        newRec = Moneyset(mRec.mCode, mRec.mName, mRec.mValue,
                          mRec.mQty, mRec.mAmt)

        newName = input(f'{newRec.mCode}, {newRec.mName} \nmName is <none>: ')
        if (newName != ''):
            newRec.mName = newName
            editFlag += 1

        newValue = input(f'{newRec.mCode}, {newRec.mName}, {newRec.mValue} \nmValue is <none>: ')
        if (newValue != ''):
            newRec.mValue = int(newValue)
            editFlag += 1

        newQty = input(f'{newRec.mCode}, {newRec.mName}, {newRec.mValue}, {newRec.mQty} \nQty is <none>: ')
        if (newQty != ''):
            newRec.mQty = int(newQty)
            editFlag += 1

        newRec.mAmt = newRec.showTotalAmount()

        newMem.append(newRec)

    print(f'---end---\n')
    
    if editFlag:
        print(f'There are {editFlag:3} changed')
    else:
        print(f'All data are not changed')
        
    #input('Press Any Key')
        
    return newMem

def updateStationData(stMem):
    """(2024-09-21) Enter All Stations Data """
    clr_PIO = input("Clear PIN, POUT <y,Y> = ")
    if clr_PIO in {'y','Y'}:
        nMem = clearPassengerCounts(stMem)
    else:
        nMem = copyStationData(stMem)

    newMem = []
    editFlag = 0
    for stRec in nMem:
        print(f'\n[{stRec.showAllStationData()}]')
        newRec = Stationset(stRec.sCode,stRec.sName,stRec.sPrice,stRec.pIN,stRec.pOUT)

        newName = input(f'{newRec.sCode}, {newRec.sName} \nsName is <none>: ')
        if (newName != ''):
            newRec.sName = newName
            editFlag += 1
        
        newPrice = input(f'{newRec.sCode}, {newRec.sName}, {newRec.sPrice} \nsPrice is <none>: ')
        if (newPrice != ''):
            newRec.sPrice = int(newPrice)
            editFlag += 1
        
        newMem.append(newRec)
        
    print(f'---end---\n')
    
    if editFlag:
        print(f'There are {editFlag:3} changed')
    else:
        print(f'All data are not changed')
        
    #input('Press Any Key')
        
    return newMem


def changeMoney(chgAmt, cashIn, wlMem):
    """(2026-09-05) 
        หลักการทอนเงินโดยตรวจจากค่ามากไปค่าน้อย
        errcode = 0     is not error
        
    """
    if chgAmt < 0:
        return 1, [], copyWalletData(wlMem)

    available = copyWalletData(wlMem)
    for cash in cashIn:
        for money in available:
            if money.mCode == cash.mCode and money.mValue == cash.mValue:
                money.mQty += cash.mQty
                money.mAmt = money.showTotalAmount()
                break

    remaining = chgAmt
    chgMem = clearWalletQuantity(available)
    for money in reversed(available):
        qty = min(money.mQty, remaining // money.mValue)
        if qty:
            money.mQty -= qty
            money.mAmt = money.showTotalAmount()
            chgMem[available.index(money)].mQty = qty
            chgMem[available.index(money)].mAmt = qty * money.mValue
            remaining -= qty * money.mValue

    if remaining:
        return 2, [], copyWalletData(wlMem)

    return 0, chgMem, available

def updatePassengerInOut(frmCode, toCode, stMem, addQty=1):
    """(2024-09-24) 
        หาสถานี From และ To แล้วเพิ่ม persIN และ persOUT ไป 1 
    """
    newMem = copyStationData(stMem)
    
    #*** Check frmCode
    ifrm = 0
    i    = 0
    for sRec in newMem:
        if sRec.sCode == frmCode:
            ifrm += 1
            break
        else:
            i += 1

    #*** Check toCode
    ito  = 0
    i    = 0
    for sRec in newMem:
        if sRec.sCode == toCode:
            ito += 1
            break
        else:
            i += 1
    
    if ifrm == 0:
        errcode = 10
    else:
        errcode = 0
        
    if ito == 0:
        errcode += 1 
    
    #*** Update newMem
    if errcode == 0:
        i = 0
        for sRec in newMem:
            if sRec.sCode == frmCode:
                newMem[i].pIN += addQty
                break
            else:
                i += 1

        i = 0
        for sRec in newMem:
            if sRec.sCode == toCode:
                newMem[i].pOUT += addQty
                break
            else:
                i += 1
  
    #print(f'errcode = {errcode}')
    #print(f'*** end function ***')    
    
    return errcode, newMem


# ***** Ticket Vending Machine *****
ACCEPTED_VALUES = (1, 2, 5, 10, 20, 50, 100, 500, 1000)
MAINTENANCE_PASSWORD = 'Manop'

def findStation(stMem, number):
    """ค้นหาสถานีจากหมายเลขที่แสดงบนหน้าจอ"""
    if number.isdigit():
        index = int(number) - 1
        if 0 <= index < len(stMem):
            return stMem[index]
    return None

def showTicketResult(origin, destination, price, paid, change, status):
    """ใบเสร็จ"""
    print('\n' + '=' * 42)
    print(f'{status:^42}')
    print('=' * 42)
    print(f'\nOrigin       : {origin.sName}')
    print(f'Destination  : {destination.sName}')
    print(f'Ticket       : {price} Credits')
    print(f'Cash In      : {paid} Credits')
    print(f'Change       : {change} Credits')
    print('\nPassenger IN : +1')
    print('Passenger OUT: +1')
    print('\n' + '*' * 5 + ' Safe Journey, Trailblazer 😉✅ ' + '*' * 5)
    print('=' * 42)

def showCashList(title, cashMem):
    """แสดงเงินแยกตามชนิดและจำนวน"""
    print(title)
    for cash in cashMem:
        if cash.mQty:
            print(f'  {cash.mValue:4} Credits x {cash.mQty}')

def buyTicket(stMem, wlMem, stCol, mnCol, stFN, wlFN):
    """เลือกสถานี รับเงิน ทอนเงิน และบันทึกข้อมูลเมื่อขายสำเร็จ"""
    print('\n[Buy Tickets]\n\nAvailable Stations')
    print('-' * 42)
    for number, station in enumerate(stMem, 1):
        print(f'{number}. {station.sName:<16} Price0: {station.sPrice}')
    print('-' * 42)

    origin = None
    while origin is None:
        choice = input('\nSelect Origin (1-9, c): ').strip().lower()
        if choice == 'c':
            return wlMem
        origin = findStation(stMem, choice)
        if origin is None:
            print('\nWhere are you now ?🤨, Try again.')

    destination = None
    while destination is None:
        choice = input('Select Destination (1-9, c): ').strip().lower()
        if choice == 'c':
            return wlMem
        destination = findStation(stMem, choice)
        if destination is None or destination is origin:
            destination = None
            print('\nWhere are you going ?🤨, Select Destination again.')

    price = abs(destination.sPrice - origin.sPrice)
    cashIn = []
    paid = 0
    print(f'\n{origin.sName} -> {destination.sName}, Ticket Price: {price} Credits')

    while paid < price:
        valueText = input(
            'Enter cash <1, 2, 5, 10, 20, 50, 100, 500, 1000, c>: '
        ).strip().lower()
        if valueText == 'c':
            showCashList('Cash Returned:', cashIn)
            return wlMem
        if not valueText.isdigit() or int(valueText) not in ACCEPTED_VALUES:
            print('\nAre you stupid or something ?🤨. I can not got that.❌')
            continue

        value = int(valueText)
        paid += value
        for cash in cashIn:
            if cash.mValue == value:
                cash.mQty += 1
                break
        else:
            cashIn.append(Moneyset(str(value), f'Cash{value}', value, 1, value))
        print(f'\nRemaining: {paid} Credits, Keep going 😘')

    error, changeMem, newWallet = changeMoney(paid - price, cashIn, wlMem)
    if error:
        print('\nSALE FAILED: Change is not available.')
        showCashList('\nSorry! change is not enough ❌, Cash Returned:', cashIn)
        return wlMem

    error, newStations = updatePassengerInOut(origin.sCode, destination.sCode, stMem)
    if error:
        print('\nSALE FAILED: Station data could not be updated.')
        showCashList('\nYou are boring. 🫩❌, Cash Returned:', cashIn)
        return wlMem

    stMem[:] = newStations
    saveStationData(stCol, stMem, stFN)
    saveWalletData(mnCol, newWallet, wlFN)
    showTicketResult(origin, destination, price, paid, paid - price, 'TICKET CONFIRMED')
    showCashList('Change Detail:', changeMem)
    return newWallet

def maintenance(stMem, wlMem, stCol, mnCol, stFN, wlFN):
    """เมนูแก้ไขข้อมูลสถานีและเงินในตู้"""
    if input('Maintenance Password: ') != MAINTENANCE_PASSWORD:
        print('\nWho are you ? May I eliminate you.❌')
        return stMem, wlMem

    while True:
        choice = input('\n[g] Station  [w] Wallet  [c] Close: ').strip().lower()
        if choice == 'g':
            stMem = updateStationData(stMem)
            saveStationData(stCol, stMem, stFN)
        elif choice == 'w':
            wlMem = updateWalletData(wlMem)
            saveWalletData(mnCol, wlMem, wlFN)
        elif choice == 'c':
            return stMem, wlMem
        else:
            print('\nPlease select g, w, or c.🤨')

def runMachine():
    """ควบคุมเมนูหลักของเครื่องจำหน่ายตั๋ว"""
    wlFN = 'Wallet.txt'
    stFN = 'Stations.txt'
    mnCol, wlMem = loadWalletData(wlFN)
    stCol, stMem = loadStationData(stFN)

    while True:
        print('\n' + '=' * 42)
        print(f'{'ASTRAL EXPRESS TICKET SYSTEM':^42}')
        print('=' * 42)
        print('\n[b] Buy Ticket\n[m] Maintenance\n[s] Shutdown')
        choice = input('\nSelect menu: ').strip().lower()

        if choice == 'b':
            wlMem = buyTicket(stMem, wlMem, stCol, mnCol, stFN, wlFN)
        elif choice == 'm':
            stMem, wlMem = maintenance(stMem, wlMem, stCol, mnCol, stFN, wlFN)
        elif choice == 's':
            if input('Shutdown Password: ') == MAINTENANCE_PASSWORD:
                print('See you next time, Good bye.😴')
                return
            print('\nSure that password is valid ?.😂')
        else:
            print('\nPlease select b, m, or s.🤨')

if __name__ == "__main__":
    runMachine()
    