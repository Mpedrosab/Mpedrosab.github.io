# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:13:02 2017

@author: M. Pedrosa Bustos
"""
import matplotlib.pyplot as plt
from monolayerClass import Monolayer
from IPython.core.display import display,HTML
import pandas as pd
#compare=Monolayer("Data\Old\DPPC_fix_B3.xls")
#compare.RemoveBias()
#plot=compare.PlotSimple(title="DPPC", label="Old")
path="Data/DPPC_B0413Y2/"
name="DPPC_B0413Y2"
compare=Monolayer(path+name+".xlsx")
compare.RemoveBias()

def path_to_image_html(path):
    #return '<img src="'+ path + '" height="50%" max-width="300px" >'
    return '<img src="'+ path + '" >'

pd.set_option('display.max_colwidth', None)
compare.data["IMG"]="BAMRAW/"+compare.data["BamFile"]
display(HTML(compare.data.to_html(escape=False ,formatters=dict(image=path_to_image_html))))
columnsShow=['Mma[A^2/molec]',	'SP[mN/m]', "IMG","BamFile"]

pd.set_option('colheader_justify', 'center')

plot=compare.PlotSimple(label="DPPC 25 $^o$C")
plot[0].savefig(path+"isotherm.png")
#compare.data["IMG"].iloc[0]="isotherm.png"

html_string = '''
<!DOCTYPE html>
<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="../../Codes/df_style.css"/>
  <body>
  <div class="title isotherm_data"><h2>
  '''
html_string+=name
html_string+= '''
  </h2>
  <img src="myIMG" height="100%"></div>
  <div class="div_isotherm_data">
    {table}
    </div>
  </body>
</html>
'''
html_string=html_string.replace("myIMG","isotherm.png")

with open(path+name+'.html', 'w') as f:
    f.write(html_string.format(table=compare.data.to_html(escape=False, classes='isotherm_data',columns=columnsShow, formatters=dict(IMG=path_to_image_html),
        na_rep="",index=False)))
'''
compare.data.to_html(, escape=False, 
        columns=columnsShow, formatters=dict(IMG=path_to_image_html),
        na_rep="",
        classes=myClass)
'''

'''
myMonolayer=Monolayer("Data\Old\Chol_B2(sph).xls" )

myMonolayer.RemoveBias()
plot=myMonolayer.PlotSimple(figure=plot,label="Old")

myMonolayer=Monolayer("Data\Old\Chol_B4_areafix_witherr_mean.xls" )

myMonolayer.RemoveBias()
plot=myMonolayer.PlotSimple(figure=plot,label="Old")
'''

plt.show()