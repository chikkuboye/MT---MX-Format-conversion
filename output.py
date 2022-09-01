# import pandas as pd
from curses import window
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import filedialog
def openFile():
    filepath = filedialog.askopenfilename()
    #with open(filepath) as file:
     #   read = file.readline()
    file = open(filepath,'r')
    read = file.readlines()

    l = ['20:','23B','33B','50K','50A','59:']
    l1 = ['{',':','-']
    l2 = []
    main_list = []

    for line in read:
        #print(line[1:4])
        if line[1:4] in l:
                #print(line[4:])
            l2.append(line[4:])
        elif line[1].isalpha():
                #print(line[:])
            l2.append(line[:])
        elif line[0] not in l1:
            l2.append(line[:])

    for i in l2:
            #a = i.strip()
            #print(a)
        main_list.append(i.strip())

    for i in main_list:
        if i == 'FOOAESMMXXX':
            main_list.remove(i)
    # print(main_list)
    line1 = main_list[0]
    line2 = main_list[1][1:]
        # line3 = main_list[2][1:]
    line4 = main_list[3][1:]
    line5 = main_list[4]
    line6 = main_list[5] + ' ' + main_list[6]
    line7 = main_list[8]
    line8 = main_list[7]

    line3w = main_list[2][1:]
    num = line3w[3:9]

    data = ET.Element('Document')

    element1 = ET.SubElement(data, 'FIToFICstmrCdtTrf')

        # Adding subtags under the `Opening`
        # subtag
    s_elem1 = ET.SubElement(element1, 'CdtTrfTxInf')
    su_elem2 = ET.SubElement(s_elem1 , 'PmtId')
    su_elem11 = ET.SubElement(su_elem2 , 'InstrId')
    su_elem11.text = line1#df1.iloc[:1].values[0][0]
    su_elem3 = ET.SubElement(s_elem1 , 'PmtTpInf')
    sub_elem1 = ET.SubElement(su_elem3 , 'LclInstrm')
    subt_elem1 = ET.SubElement(sub_elem1 , 'Prtry')
    subt_elem1.text = line2#df1.iloc[1:].values[0][0]
        # s_elem2 = ET.SubElement(element1, 'D4')
    su_elem4 = ET.SubElement(s_elem1 , 'IntrBkSttlmAmt')

    su_elem4.text = num#df1.iloc[2:].values[0][0]
    su_elem5 = ET.SubElement(s_elem1 , 'Dbtr')
    sub_elem2 = ET.SubElement(su_elem5 , 'Nm')
    sub_elem2.text = line5 #df1.iloc[4:].values[0][1]
    sub_elem3 = ET.SubElement(su_elem5 , 'PstlAdr')
    subt_elem2 = ET.SubElement(sub_elem3 , 'AdrLine')
    subt_elem2.text = line6 #df1.iloc[4:].values[1][1]#subt_elem2.text = df1.iloc[4:].values[2][1])
        #subt_elem2.text = df1.iloc[4:].values[2][1] 
    su_elem6 = ET.SubElement(s_elem1 , 'DbtrAcct')
    sub_elem4 = ET.SubElement(su_elem6 , 'Id')
    subt_elem3 = ET.SubElement(sub_elem4 , 'Othr')
    subte_elem1 = ET.SubElement(subt_elem3 , 'Id')
    subte_elem1.text = line4 #df1.iloc[2:].values[1][0]
    su_elem7 = ET.SubElement(s_elem1 , 'Cdtr')
    sub_elem5 = ET.SubElement(su_elem7 , 'Nm')
    sub_elem5.text= line7 #df1.iloc[6:].values[2][1]

    su_elem8 = ET.SubElement(s_elem1 , 'CdtrAcct')
    sub_elem6 = ET.SubElement(su_elem8 , 'Id')
    subt_elem4 = ET.SubElement(sub_elem6 , 'Othr')
    subte_elem2 = ET.SubElement(subt_elem4 , 'Id')
    subte_elem2.text = line8 #df1.iloc[6:].values[1][0]


    b_xml = ET.tostring(data)

        # Opening a file under the name `items2.xml`,
        # with operation mode `wb` (write + binary)
    with open("MXFormat.xml", "wb") as f:
        f.write(b_xml)

    with open('MXFormat.xml', 'r') as f:
        data = f.read()
            
    bs_data = BeautifulSoup(data, 'xml')
    print(bs_data.prettify())

    #print(main_list)    # file.close()

window = Tk()
button = Button(text="open",command=openFile)
button.pack()
window.mainloop()

# print(main_list)
