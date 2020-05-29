a = [] 
p = [] 
while True:
    m = input('*******mumu shop*******\nกดเลือกสินค้า 1 2 3 4 Exit 5 Bin 6\n1.Nike      *1*\n2.Adidas    *2*\n3.Reebok    *3*\n4.Vans      *4*\n5.Exit      *5*\n6.Bin       *6*\n')
    if m=='1':
        n = input('----------Nike----------\n1)Air Jordan 1 Mid SE              3,680 บาท\n2)Nike React Infinity Run Flyknit  4,640 บาท\n3)Nike Zoom X Vista Grind          4,600 บาท\n')
        if n=='1':
            ms = ('Air Jordan 1 Mid SE               4,600 บาท     20%     3,680 บาท ')
            ps = 3680 
            print(input('Air Jordan 1 Mid SE        ราคา 4,600 บาท    ลด 20%    จ่ายจริง 3,680 บาท'))
            a.append(ms)
            p.append(ps)
        elif n=='2':
            ir = ('Nike React Infinity Run Flyknit   5,800 บาท     20%     4,640 บาท ')
            pf = 4640
            print(input('Nike React Infinity Run Flyknit        ราคา 4,600 บาท    ลด 20%    จ่ายจริง 4,600 บาท'))
            a.append(ir)
            p.append(pf)
        elif n=='3':
            zv = ('Nike Zoom X Vista Grind           5,800 บาท     20%     4,640 บาท ')
            pz = 4640
            print(input('Nike Zoom X Vista Grind        ราคา 4,600 บาท    ลด 20%    จ่ายจริง 4,600 บาท'))
            a.append(zv)
            p.append(pz)
        else:
            input('กรุณากด Enter เพื่อเริ่มรายการใหม่')
            
    if m=='2':
        ad = input('----------adidas----------\n1)SUPERSTAR FOUNDATION   2,240 บาท\n2)SUPERSTAR              3,710 บาท\n3)ULTRABOOST X           5,600 บาท\n')
        if ad=='1':
            ms = ('SUPERSTAR FOUNDATION              3,200 บาท     30%     2,240 บาท ')
            ps = 2240
            print(input('SUPERSTAR FOUNDATION        ราคา 3,200 บาท    ลด 30%    จ่ายจริง 2,240 บาท'))
            a.append(ms)
            p.append(ps)
        elif ad=='2':
            ir = ('SUPERSTAR                         5,300 บาท     30%     3,710 บาท ')
            pf = 3710
            print(input('SUPERSTAR        ราคา 5,300 บาท    ลด 30%    จ่ายจริง 3,710 บาท'))
            a.append(ir)
            p.append(pf)
        elif ad=='3':
            zv = ('ULTRABOOST X                      8,000 บาท     30%     5,600 บาท ')
            pz = 5600
            print(input('ULTRABOOST X        ราคา 8,000 บาท    ลด 30%    จ่ายจริง 5,600 บาท'))
            a.append(zv)
            p.append(pz)
        else:
            input('กรุณากด Enter เพื่อเริ่มรายการใหม่')
            
    if m=='3':
        r = input('----------Reebok ----------\n1)AHARY RUNNER          1,470 บาท\n2)REEBOK ROYAL GLIDE    1,650 บาท\n3)FSTR FLEXWEAVE        1,470 บาท\n')
        if r=='1':
            ms = ('AHARY RUNNER                      4,900 บาท     70%     1,470 บาท ')
            ps = 1470
            print(input('AHARY RUNNER        ราคา 4,900 บาท    ลด 70%    จ่ายจริง 1,470 บาท'))
            a.append(ms)
            p.append(ps)
        elif r=='2':
            ir = ('REEBOK ROYAL GLIDE                5,500 บาท     70%     1,650 บาท ')
            pf = 1650
            print(input('REEBOK ROYAL GLIDE        ราคา 5,500 บาท    ลด 70%    จ่ายจริง 1,650 บาท'))
            a.append(ir)
            p.append(pf)
        elif r=='3':
            zv = ('FSTR FLEXWEAVE                    4,900 บาท     70%     1,470 บาท ')
            pz = 1470
            print(input('FSTR FLEXWEAVE       ราคา 4,900 บาท    ลด 70%    จ่ายจริง 1,470 บาท'))
            a.append(zv)
            p.append(pz)
        else:
            input('กรุณากด Enter เพื่อเริ่มรายการใหม่')      
    if m=='4':
        V = input('----------Vans----------\n1)Van1              3,680 บาท\n2)Van2              4,640 บาท\n3)Van3              4,600 บาท\n')
        if V=='1':
            ms = ('Vans1                             4,600 บาท     20%     3,680 บาท ')
            ps = 3680 
            print(input('Vans1                ราคา 4,600 บาท    ลด 20%    จ่ายจริง 3,680 บาท'))
            a.append(ms)
            p.append(ps)
        elif V=='2':
            ir = ('Vans2                             5,800 บาท     20%      4,640 บาท ')
            pf = 4640
            print(input('Vans2                ราคา 4,600 บาท    ลด 20%    จ่ายจริง 4,600 บาท'))
            a.append(ir)
            p.append(pf)
        elif V=='3':
            zv = ('Vans3                             5,800 บาท     20%      4,640 บาท ')
            pz = 4640
            print(input('Vans3                ราคา 4,600 บาท    ลด 20%    จ่ายจริง 4,600 บาท'))
            a.append(zv)
            p.append(pz)
        else:
            input('กรุณากด Enter เพื่อเริ่มรายการใหม่')
    if m== '5': #ออกจากระบบ
        print('ขอบคุณที่มาใช้บริการค่ะ')
        break
    if m== '6': #bin
        print('ยอดที่ต้องชำระ')
        print('{0:-<40}{1:-<15}{2:-<10}{3:<10}'.format('รุ่น','ราคา','ลด','จ่ายจริง'))
        print('{0:-<65}'.format("ggg"))
        count = 0
        for d in a:
            count += 1 #ลำดับที่
            print(count,end=") ") 
            print(d)
        
        print('{0:-<65}'.format(""))
        sum = 0
        for n in p:
            sum += n
        print('รวมเป็นเงิน                                                ', sum,'บาท')
    
        print('{0:-<65}'.format(""))
        print('\n')
        input('กด Enter เพื่อดำเนินการต่อ')