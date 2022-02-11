import subprocess
import re
import os

def refresh_information():
    print("Refreshing...")
    final=[]
    data=str(subprocess.check_output(['hwinfo', '--monitor'])).split("\\n\\n")
    for mon in data:
        ret={}
        ret["size"]=re.findall('Size: (\d+)x(\d+) mm', mon)[0]
        ret["resolution"]=re.findall('     Resolution: (\d+x\d+)', mon)[0]
        ret["vendor"]=re.findall('Vendor: (["\w\s]+)', mon)[0].replace("\"", "").split()[-1]
        ret["ID"]=re.findall('Unique ID: ([\w.]+)', mon)[0]
        final.append(ret)
    return final




def flushQueue(queue): 
    print("Printing...")
    num=0
    header = '''<!DOCTYPE html>                                                    
                <html>
                <body>'''
    footer=''' </body>
                </html> '''
    body='''
    <h1 style="font-family:sans-serif;
    position:relative; text-align:center; font-size:80px; top:0px; margin-top: 0px; margin-bottom: 0px">{}</h1>

    <p class="res" style="font-family:sans-serif;
    position:relative; text-align:center; font-size:60px; top:0px; margin-top: 0px; margin-bottom: 0px"><b>{}</b></p>

    <p class="interfaces" style="font-family:sans-serif;
    position:relative; text-align:center; font-size:60px; top:0px; margin-top: 0px; margin-bottom: 0px"><b>{}</b></p>
    
    <br>
    <br>
    '''
    doc=header
    for mon in queue:
        if(num<5):
            HTML_TITLE = '{} {}" Monitor'.format(mon["vendor"], mon["size"])
            HTML_DIM = mon["resolution"]
            HTML_INT = mon["interfaces"]
            doc += body.format(HTML_TITLE, HTML_DIM, HTML_INT)
            num+=1
        else:
            doc+=footer
            htmlFile = open("./temp.html", 'w')
            htmlFile.write(doc)
            htmlFile.close()
            os.system("wkhtmltopdf ./temp.html temp.pdf")
            os.system("lpr -P HP-LaserJet-P2015-Series temp.pdf")
            doc=header
            num=0
    if(num>0):
        doc+=footer
        htmlFile = open("./temp.html", 'w')
        htmlFile.write(doc)
        htmlFile.close()
        os.system("wkhtmltopdf ./temp.html temp.pdf")
        os.system("lpr -P 'hp-LaserJet-1320-series' temp.pdf")


