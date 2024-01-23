from sys import modules, path
import sys
if globals(  ).has_key('init_modules'):
    # second or subsequent run: remove all but initially loaded modules
    for m in sys.modules.keys(  ):
        if m not in init_modules:
            del(sys.modules[m])
else:
    # first run: find out which modules were initially loaded
    init_modules = sys.modules.keys(  )
    
from sys import path
path.append('/home/mariapb/IsothermData/Codes')
path.append('/home/mariapb/IsothermData/Data')
#print(listdir("/home/mariapb/IsothermData/Codes"))

from ImgJClass import imgJClass

from java.lang.System import getProperty
from ij import IJ, ImagePlus,ImageStack
from ij.process import FloatProcessor,ByteProcessor
# extend the search path by $FIJI_ROOT/bin/
from array import array
select="OpenFromJython"			#PolyfitSub,CheckSign,OpenFromJython

if (select=="None"):
	print("No selection")
	###################################################
	#Open FROM PYTHON
elif (select=="OpenFromJython"):
	print("***** Option OpenFromJython *****")
	
	path="../Data/DPPC_B0428N25/BAMRAW/BG_Stack0137.jpg"
	path="/home/mariapb/IsothermData/Data/DPPC_B0428N25/BAMRAW/106539601065000.jpg"
	imp=IJ.openImage(path)
	imp.show()
	IJ.run("Show Info...")
	pixels=imp.getProcessor().getPixels()
	pixels2=map(lambda p: p[0], zip(pixels))
	pixels3=array("b",pixels2)

	#pixels3=pixels3.fromlist(pixels2)
	print(min(pixels),max(pixels))
	print(imp.getProcessor().getMin(),imp.getProcessor().getMax())
	
	#for i in range(0,len(pixels)/2):
	#	pixels[i]=pixels[i]*10
	imp2=ImagePlus("h", ByteProcessor(imp.getProcessor().getWidth(), imp.getProcessor().getHeight(), pixels3))
	imp2.show()
	IJ.run("Show Info...")
	print(pixels.typecode)
	imp2=IJ.getImage()
	pixels=imp.getProcessor().getPixels()
	print(min(pixels),max(pixels))

	#######################################
elif (select=="OpenStack"):
	print("***** Option OpenStack *****")
	ijc=imgJClass()
	path="D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/"
	names, myStack=ijc.getStackNames(path,substring="BG_Stack")
	ImagePlus("Stack", myStack).show()
	##########################################
	# CHECK SIGN
	
elif (select=="CheckSign"):
	print("***** Option CheckSign *****")

	ijc=imgJClass()
	
	path="D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/test.txt"
	imp=ijc.txtToImg(path)
	#imp=ijc.ToUnsigned(imp)
	#imp=IJ.openImage(path)
	imp.show()
	pixelsScList=imp.getProcessor().getPixels()
	print("**Scientific img**")
	print("Pixel Min/max",min(pixelsScList),max(pixelsScList))
	print("Processor Min/max",imp.getProcessor().getMin(),imp.getProcessor().getMax())
	IJ.run(imp,"Polynomial Surface Fit", "order=3 order_0=3")
	imBack1 = IJ.getImage()
	pixelsRef=imBack1.getProcessor().getPixels()
	print("**BG img**")
	print("Pixel Min/max",min(pixelsRef),max(pixelsRef))
	print("Processor Min/max",imBack1.getProcessor().getMin(),imBack1.getProcessor().getMax())
	
	i=0
	reslt2=ijc.SubtractBasic(imBack1,imp,"/")
	result=[]
	for pixelRef in pixelsRef:
		pixelSc=pixelsScList[i]
	
		result.append(pixelSc/pixelRef)
		i+=1		
	pixelResult=reslt2.getProcessor().getPixels()
	print("**Subtract result raw**")
	print("Pixel Min/max",min(pixelResult),max(pixelResult))
	reslt2.show()
	resultimg=ImagePlus("h", FloatProcessor(imp.getProcessor().getWidth(), imp.getProcessor().getHeight(), result))
	resultimg.show()
	
	resultimg2=IJ.getImage()
	pixelResult=resultimg2.getProcessor().getPixels()
	print("**Subtracted img**")
	print("Pixel Min/max",min(pixelResult),max(pixelResult))
	print("Processor Min/max",resultimg2.getProcessor().getMin(),resultimg2.getProcessor().getMax())
	
	resultimg2Unsing=ijc.ToUnsigned(resultimg2)
	print("**Subtracted img Unsigned**")
	print("Pixel Min/max",min(resultimg2Unsing.getProcessor().getPixels()),max(resultimg2Unsing.getProcessor().getPixels()))
	print("Processor Min/max",resultimg2Unsing.getProcessor().getMin(),resultimg2Unsing.getProcessor().getMax())
	resultimg2Unsing.show()
	#print(result)

	###############################################
	# GET SELECTION
	'''
	from ij import IJ, ImagePlus,ImageStack
	from ij.plugin.frame import RoiManager
	from ij.gui import WaitForUserDialog, Toolbar
	path="D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/106539608817000.jpg"
	imp=IJ.openImage(path)
		
	IJ.setTool(Toolbar.RECTANGLE)
	
	WaitForUserDialog("Select the area,then click OK.").show();
	roi1 = imp.getRoi()
	
	bounds = roi1.getProcessor().getPixels()
	print(len(bounds))
	'''
	#############################################33
	#REMOVE SIGN 
	'''
	elif (select=="RemoveSign"):
		# https://forum.image.sc/t/converting-16-bit-signed-tiffs-to-16-bit-unsigned/5847/3 
		from ImgJClass import imgJClass
		ijc=imgJClass()
		stack=ijc.ChangeMin("Result-1")
		for i in range (1,stack.getSize()+1, 1):
			ip = stack.getProcessor(i)
			#print(ip.getMin(),ip.getMax())
			
		ImagePlus("Result2", stack).show()
		path="D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/Subtrac_Stack0053.jpg"
		imp=IJ.openImage(path)
		print(imp.getStatistics())
		improc=imp.getProcessor()
		print(improc.getMin(),improc.getMax())
		minimg=improc.getMin()
		maximg=improc.getMax()
		improc.setMinAndMax(minimg-100, maximg-100)
		print(improc.getMin(),improc.getMax())
		pixels=improc.getPixels()
		pixels=map(lambda p: p[0], zip(pixels))
		#print(pixels)
		imp=ImagePlus("Result", FloatProcessor(improc.getWidth(), improc.getHeight(), pixels))
		print(imp.getStatistics())
		ijc.IMGtoTxt(imp,path.replace("jpg","txt"))
	'''
	
	'''
	#filePath = "D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/"
	ijc=imgJClass()
	myPath = "D:\\Documentos_D\\Google_Drive_UGR\\Data_analysis\\Data\\DPPC_B0428N25\\BAMRAW\\"
	BGNames=ijc.getStackNames(myPath,substring="BG_Stack")
	IMGNames=ijc.getStackNames(myPath,substring="1065")
	
	[result1,result2]=ijc.NormalizeIntensity(IMGNames, BGNames,path=myPath)
	img.show()
	result=img.getStatistics()
	print(result)
	
	#for i in range(1, test.getNSlices()+1):
	#	print("yes")
	#test.close()
	t=test.getProcessor(1)
	'''	
	##################################################33
	#Get BG and subtract each img from its BG with polyfit
elif (select=="PolyfitSub"):
	ijc=imgJClass()
	
	filePath = "D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/Test/DPPC/"
	filePath = "/home/mariapb/IsothermData/Data/Test/DPPC/"
	#myFiles=ijc.getStackNames(filePath)
	myFiles=[
				"DPPC_B0428N25Raw8bit.jpg",
	]
	
	i=0
	for files in myFiles:
		imp=IJ.openImage(filePath+files)
		
		if i==0:
			imp=ijc.ToUnsigned(imp)
			impBack=imp
			
			IJ.run(impBack,"Polynomial Surface Fit", "order=3 order_0=3")
			imBack1 = IJ.getImage()
			imBack1=IJ.openImage(filePath+files.replace("Raw8","_BG32").replace("jpg","tiff"))
			#imBack2.show()
			#imBack2=ijc.ToUnsigned(imBack1)
			imBack2=imBack1
			
			imBack2Pixel = imBack2.getProcessor().getPixels()
			imBack2Pixel=zip(imBack2Pixel)
			imBack2Pixel=[x[0] for x in imBack2Pixel]
			imBack2Data=[imBack2Pixel,impBack.getProcessor().getWidth(),impBack.getProcessor().getHeight()]
			impStack=ImageStack(imBack2Data[1],imBack2Data[2])
			impStackFlat=ImageStack(imBack2Data[1],imBack2Data[2])
			impStackFlatDiv=ImageStack(imBack2Data[1],imBack2Data[2])
			impStackBack=ImageStack(imBack2Data[1],imBack2Data[2])
			imBack1.close()
			i+=1
		myTitle=files.replace(".png","_flat.png")
		myTitleBack=files.replace(".png","_bg.png")
		#impSubtract=SubstractFromTxt(ToUnsigned(imp), imBack2Data[0])
		#impSubtract=ImagePlus(myTitle, FloatProcessor(imBack2Data[1], imBack2Data[2], impSubtract))
		impStack.addSlice(files,imp.getProcessor())
		IJ.run(imp,"Polynomial Surface Fit", "order=3 order_0=3")
		impBackNow1 = IJ.getImage()
	
		#impBackNow=ijc.ToUnsigned(impBackNow1)
		impBackNow=impBackNow1
		
		impStackBack.addSlice(myTitleBack,impBackNow.getProcessor())
		#impBackNow=SubstractFromTxt(ToUnsigned(impBackNow), imBack2Data[0])
		#impSubtract=ijc.SubtractBasic(impBackNow, ijc.ToUnsigned(imp),title=myTitle)
		impSubtract=ijc.SubtractBasic(impBackNow, imp,"-",title=myTitle)
		impSubtractDiv=ijc.SubtractBasic(impBackNow, imp,"/",title=myTitle)
		impStackFlat.addSlice(myTitle,impSubtract.getProcessor())
		impStackFlatDiv.addSlice(myTitle,impSubtractDiv.getProcessor())
		impBackNow1.close()		
	
	ImagePlus("Initial Stack", impStack).show()
	ImagePlus("Subtracted Stack", impStackFlat).show()
	ImagePlus("SubtractedDiv Stack", impStackFlatDiv).show()
	ImagePlus("Background Stack", impStackBack).show()



#########################################################
#Subtract each mean and then resize by BG mean
'''
elif (select==3):
	import sys
	sys.modules.clear()
	from sys import path
	from java.lang.System import getProperty
	from ij import IJ, ImagePlus,ImageStack
	
	# extend the search path by $FIJI_ROOT/bin/
	path.append("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Codes")
	
	from ImgJClass import imgJClass
	
	ijc=imgJClass()
	
	filePath = "D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/Chol_B0414Y25/BAMRAW/"
	myFiles=ijc.getStackNames(filePath)
	
	myFiles=ijc.getStackNames(filePath,substring="BG_Stack")
	[meanAll,maxAll,minAll]=ijc.StoreStatInArray(myFiles,path=filePath)
	print([meanAll,maxAll,minAll])
	myFiles=ijc.getStackNames(filePath,substring="Sub_Stack")
	myStack=ijc.CalculatorArray(myFiles,meanAll,"*",path=filePath)
	print("ok")
	ImagePlus("Result2", myStack).show()


'''
###################################
'''
[img,txtData]=txtToImg("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/background.txt")
impRef=IJ.openImage("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N20/BAMRAW/106539468591300.jpg")
result=SubstractFromTxt( ToUnsigned(impRef),txtData)
IMGtoTxt([result,impRef.getWidth(),impRef.getHeight()],"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/result.txt")
result=ImagePlus(impRef.getTitle(),FloatProcessor(impRef.getWidth(),impRef.getHeight(), result))
result=ToUnsigned(result)
result.show()
IMGtoTxt(result,"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/result2.txt")
input("continue")
#Reference image
impRef = IJ.openImage("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/BAMRAW/background.jpg")
#impRef=ToUnsigned(impRef)
result=SubstractMax(impRef, ToUnsigned(impRef))
IMGtoTxt(impRef,"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N25/flat.txt")
impRef = IJ.openImage("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N20/BAMRAW/106539468591300.jpg")
impRef.show()
impRef=ToUnsigned(impRef)
IMGtoTxt(impRef,"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/impRef.txt")
#impRef.show()

#Data IMG
impSc = IJ.openImage("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/DPPC_B0428N20/BAMRAW/106539470795600.jpg")
#impSc = IJ.openImage("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/Chol_W1/BAMRAW/106478562529300.jpg")
impSc.show()
impSc=ToUnsigned(impSc)
IMGtoTxt(impSc,"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/impSc.txt")
result=SubstractMax(impRef, impSc)
#result=ToUnsigned(result)
#result=ToUnsigned(result)
IMGtoTxt(result,"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/result.txt")
print("Finish")

#print(result[0]+result[1]+result[2])
#print(640*480)
result.show()
'''

###############################################
#Test for unsigned command
'''
import sys
sys.modules.clear()
from sys import path
from java.lang.System import getProperty
from ij import IJ, ImagePlus,ImageStack
from ij.process import FloatProcessor

# extend the search path by $FIJI_ROOT/bin/
path.append("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Codes")

from ImgJClass import imgJClass
ijc=imgJClass()
original=ijc.txtToImg("D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/result.txt")
print(original.getStatistics())
result=ijc.ToUnsigned(original)
print(result.getStatistics())
pix2=result.getProcessor().convertToFloat().getPixels()

pix2 = map(lambda x: x - 3, pix2)
result2=ImagePlus("min subtracted", FloatProcessor(original.width, original.height, pix2))
result2.show()

ijc.IMGtoTxt(result2,"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/resultUnsigned.txt")
'''