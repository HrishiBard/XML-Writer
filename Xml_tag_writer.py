import re
import os
from xml.etree import ElementTree

path = os.getcwd()+"\\"
prefFile = path+'prefval.txt'
writexml = path+'xmlwrite.xml'
print(prefFile)
preferenceWriter = open(prefFile,'a+')
prefTrue = os.path.isfile(prefFile)
readMode = open(prefFile,'r')
allLines = readMode.readlines()
firstLine = False
prefVal = False
header = []
value = []


try:
    if len(allLines[0]) > 0: 
        H1 = allLines[0].split("|")
        for h in H1:
            header.append(h)
        firstLine = True
    if len(allLines[1:]) > 0:
        prefVal = True
        for line in allLines[1:]:
            V1 =line.split('|')
            value.append(V1)
        
except:
    pass

total = len(allLines[1:])
total = total -1
defaultTage = """<Site id="" name="" siteId="">
<ApplicationRef application="" label="" version=""></ApplicationRef>
<UserData id="">
<UserValue title="" value=""></UserValue>
</UserData>
</Site>"""

class mainClass():

    def main(self):
    
        val = 0
        root = ElementTree.fromstring(defaultTage)
        
        for elem in root.iter():
            if firstLine == False:
                if len(elem.attrib) > 0:
                    for attr in elem.attrib:
                         preferenceWriter.write(str(elem.tag)+":"+str(attr)+"|")    
                else:
                    preferenceWriter.write(elem.tag+"|") 
        
            if prefVal == True:
                while  val <= total:
                    cout = 0
                    for elem in root.iter():
                        if len(elem.attrib) > 0: 
                            for attr in elem.attrib:
                                if str(elem.tag)+":"+str(attr) in header:
                                    elem.attrib[str(attr)] = value[val][cout]
                                    cout = cout +1
                                
                        else:
                            elem.text = value[val][cout]
                            cout = cout +1
                      
                    val = val +1
                    tree = ElementTree.ElementTree(root)
                    with open (writexml, 'ab') as files : 
                        tree.write(files)
                    ElementTree.dump(root)

if __name__ == '__main__':
    mainClass = mainClass()

    mainClass.main()