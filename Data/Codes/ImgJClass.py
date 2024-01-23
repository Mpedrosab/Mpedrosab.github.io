# The module __future__ contains some useful functions:
# https://docs.python.org/2/library/__future__.html
# By adding an asterisk to a parameter, all given parameters are combined to a tuple.
#
#util scripts: https://imagej.net/Jython_Scripting_Examples 
from __future__ import with_statement, division
from ij import ImagePlus
from ij.process import FloatProcessor,ByteProcessor
from ij.plugin.frame import RoiManager
from ij.gui import WaitForUserDialog, Toolbar
from ij import IJ,ImageStack, WindowManager
from os import listdir
import sys		



class imgJClass():
	def __init__(self):
		self.windowsID=self.getOpenWindowID()
		return
		
	def computeMean(self,pixels):
	  return sum(pixels) / float(len(pixels))
 
	def computeStdDev(self,pixels, mean):
	  s = 0
	  for i in range(len(pixels)):
	    s += pow(pixels[i] - mean, 2)
	  return sqrt(s / float(len(pixels) -1))

	def getOpenWindowID(self):
		myIds={}
		alreadyFound=[]
		allWindows=WindowManager.getIDList()
		if allWindows is None:
			return {"None":"None"}
		for id in WindowManager.getIDList():
			myTitle=WindowManager.getImage(id).getTitle()
			if myTitle in alreadyFound:
				myTitle=myTitle+"_2"
			myIds[myTitle]=id
			alreadyFound.append(myTitle)
			
		return myIds
		
	def img_calc(self,func, *imps, **kwargs):
		"""Runs the given function on each pixel of the given list of images.
		An additional parameter, the title of the result, is passed as keyword parameter.
		We assume that each image has the same size. This is not checked by this function.
		"""
		# If the keyword parameter is not passed, it is set to a default value.
		if not kwargs['title']:
			kwargs['title'] = "Result"
		# This is a 2D list: list[number of images][pixels per image] .
		pixels = [imp.getProcessor().getPixels() for imp in imps]
		# The function is called pixel by pixel.
		# zip(*pixels) rotates the 2D list: list[pixels per image][mumber of images].
		result = [func(vals) for vals in zip(*pixels)]
		# result is a 1D list and can be used to create an ImagePlus object.

		return ImagePlus(kwargs['title'], FloatProcessor(img_size, img_size, result))
	
	def GetPositionIndex(self,index,width, height):
		col=index%width
		row=index // width
		return [row,col]
	
	def toMatrix(data):
		'''
			List with [pixel,width,height] or Image object
	
		'''
		
		i=0
		dataOut=[]
		if type(data)!=list:
			width=data.getWidth()
			height=data.getHeight()
			pixels=data.getProcessor().getPixels()
		else:
			pixels=data[0]
			width=data[1]
			height=data[2]
		
		for pixelRef in zip(pixels):
			position=self.GetPositionIndex(i, width,height)
			if position[1]!=0:		#Do not change row
				dataOut[position[0]].append(pixelRef[0])
			else:			#Change row
				dataOut.append([pixelRef[0]])
			i+=1
		return dataOut
	
	def IMGtoTxt(self,data,datafile):
		'''
			List with [pixel,width,height] or Image object
	
		'''
		i=0
		if type(data)!=list:
			width=data.getWidth()
			height=data.getHeight()
			pixels=data.getProcessor().getPixels()
		else:
			pixels=data[0]
			width=data[1]
			height=data[2]
		
		fileOut=open(datafile,"w")
		previousRow=0
		stringOut=""
		for pixelRef in zip(pixels):
			position=self.GetPositionIndex(i, width,height)
			if position[0]>previousRow:
				stringOut="\n"
				previousRow=position[0]
			elif i!=0:
				stringOut="\t"
			#stringOut+="[%d,%d]" %(position[0],position[1])
			stringOut+="%d" %(pixelRef[0])
			fileOut.write(stringOut)
			i+=1
		fileOut.close()
		return 
		
	def ToUnsigned(self,imp,convert="0xff"):
		'''
		Converting signed pixel values to unsigned 
	# & 0xff : 8bit			#negative values are mapped to 255-127
	# & 0xffff : 16bit
	# & 0xffffffff : 32bit 

	# Create an image with given format: https://imagej.net/Jython_Scripting.html#ImageJ_and_Fiji_API
			https://javadoc.scijava.org/ImageJ1/ij/IJ.html#createImage-java.lang.String-int-int-int-int-
		'''
		from ij.process import FloatProcessor
		signedpix = imp.getProcessor().getPixels()
		signedpix=[int(x) for x in signedpix]
		unsignedpix = map(lambda p: p & 0xff, signedpix)
		imp1 = IJ.createImage ('imp1',"8-bit", imp.getWidth(),imp.getHeight(), 1)
		imp1 = ImageStack()
		impPlus=ImagePlus(imp.getTitle(),FloatProcessor(imp.getWidth(),imp.getHeight(), unsignedpix))
		imp1.addSlice(impPlus.getProcessor())
		result=imp1.getProcessor(1)
		#print(type(unsignedpix))
		#imp1.getProcessor().getPixels()=unsignedpix
		#ImagePlus("Result2", imp1).show()
		return impPlus

	def ChangeMin(self,stackName):
		# This script implements the Plugins>Filters>Signed 16-bit
		# to Unsigned command, which converts signed 16-bit 
		# images and stacks to unsigned. (TO THE MIN OF THE HOLE STACK!!)
		#https://forum.image.sc/t/converting-16-bit-signed-tiffs-to-16-bit-unsigned/5847/3
		
		imp = WindowManager.getImage(self.windowsID[stackName])
		print(type(imp))
		print("########################################")
		stack = imp.getStack()
		if (stack.isVirtual()):
			IJ.error("Non-virtual stack required")
		cal = imp.getCalibration()
		print(cal)
		#if (cal.isSigned()==False):
		#	IJ.error("Signed 8-bit image required")
		cal.disableDensityCalibration()
		ip = imp.getProcessor()
		ip=ip.convertToFloat()
		minVal = ip.getMin()
		maxVal = ip.getMax()
		
		stats = imp.getStatistics()
		minv = stats.min
		minv=10000
		newStack=ImageStack(ip.getWidth(),ip.getHeight())
		ip = stack.getProcessor(stack.getSize())
		size=[ip.getWidth(),ip.getHeight()]
		self.IMGtoTxt([ip.getPixels(),size[0],size[1]],"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/borrarPrev.txt")
		print(ip.getMin(),ip.getMax())
		for i in range (1,stack.getSize()+1, 1):
			ip = stack.getProcessor(i)
			#ip=ip.convertToFloat()
			#ip.add(-minv)
			#ip.add(-minv)
			ip.setMinAndMax(minVal-minv, maxVal-minv)
			newStack.addSlice(ip)
			#newStack.addSlice(
		imp.setStack(stack)
		print(ip)
		myIMG=ImagePlus("title", FloatProcessor(size[0],size[1],[x[0] for x in zip(ip.getPixels())]))
		myIMG.show()
		print("########################################")
		self.IMGtoTxt([ip.getPixels(),ip.getWidth(),ip.getHeight()],"D:/Documentos_D/Google_Drive_UGR/Data_analysis/Data/borrarAfter.txt")
		#print(IJ.run(newStack,"Statistics"))
		ip = imp.getProcessor()
		
		#imp.updateAndDraw()
		return newStack
	
	def LevelToZero(self,img):
		imgDim=[img.getWidth(),img.getHeight()]
		pixels =img.getProcessor().getPixels()
		pixels=zip(pixels)[:,0]
		maxPixel=max(pixels)
		minPixel=min(pixels)
		
		for i in range (0,len(pixels)):
			pixels[i]=pixels[i]-minPixel
		return ImagePlus(imp.getTitle()+"_toZero", FloatProcessor(imgDim[0], imgDim[1], pixels))
		
	def SubstractMax(self,impRef, impSc,**kwargs):
		imgRefDim=[impRef.getWidth(),impRef.getHeight()]
		imgimpScDim=[impSc.getWidth(),impSc.getHeight()]
	
		if (imgRefDim[0]!=imgimpScDim[0]) or (imgRefDim[1]!=imgimpScDim[1]):
			print("Not same size")
			return
		if "title" not in kwargs:
			kwargs['title'] = "Result"
			
		pixelsRef = impRef.getProcessor().getPixels()
		pixelsSc = impSc.getProcessor().getPixels()
		pixelsScList=zip(pixelsSc)
		i=0
		result=[]
	
		in1=0
		in2=0
		in3=0
	
		for pixelRef in zip(pixelsRef):
	
			#print((pixelRef[0],))
			#i+=1
			
			pixelSc=pixelsScList[i]
			i+=1
			if len(pixelRef)!=1 or len(pixelSc)!=1:
				raise TypeError("Not a gray image")
	
			'''
			if (pixelSc[0]<pixelRef[0]):		#Can not happend
				result.append(pixelSc[0])
				#resultFake.append(100)
	
				in2+=1			
			#if pixelSc[0]<=pixelRef[0]:
			elif ((pixelSc[0]>(pixelRef[0]+10)) and (pixelRef[0]>64)):
				result.append(pixelSc[0])
				#resultFake.append(255)
				in1+=1
	
			  	
			else:
				result.append(pixelSc[0]-pixelRef[0])
				#resultFake.append(0)
				in3+=1
			'''
			value=pixelSc[0]-pixelRef[0]
			result.append(value)
	
		threshold=min(result)
		print(threshold)
		result=[x-threshold for x in result]
		
		# result is a 1D list and can be used to create an ImagePlus object.
		print("Result substraction")
		#print(result)
		print(in1, in2, in3)
		#fakeImg=ImagePlus(kwargs['title'], FloatProcessor(imgRefDim[0], imgRefDim[1], resultFake))
		#fakeImg.show()
		#fakeImg2=ImagePlus(kwargs['title'], FloatProcessor(imgRefDim[0], imgRefDim[1], f))
		#fakeImg2.show()
		#return [in1, in2, in3]
		
		return ImagePlus(kwargs['title'], FloatProcessor(imgRefDim[0], imgRefDim[1], result))
	
	def SubtractBasic(self,impRef, impSc, operation,**kwargs):
		impScDim=[impSc.getWidth(),impSc.getHeight()]
		pixelsRef = impRef.getProcessor().getPixels()
		pixelsSc = impSc.getProcessor().getPixels()
		pixelsScList=zip(pixelsSc)
		i=0
		result=[]
		if "title" not in kwargs:
			kwargs['title'] = "Result"
			
		for pixelRef in zip(pixelsRef):
			pixelSc=pixelsScList[i]
			
			if len(pixelRef)!=1 or len(pixelSc)!=1:
				raise TypeError("Not a gray image")
			if (operation=="-"):
				result.append(pixelSc[0]-pixelRef[0])
			elif (operation=="/"):
				result.append(pixelSc[0]/pixelRef[0])
			
			else:
				raise TypeError("Invalid operation")
				break
			
			
			i+=1
		return ImagePlus(kwargs['title'], FloatProcessor(impScDim[0], impScDim[1], result))
		
	def txtToImg(self,txtFile):
		f=open(txtFile)
		text=f.read()
		print(text)
		f.close()
		if text[-1]=="\n":
			text=text[:-1]
		lines=text.split("\n")
		height=0
		pixels=[]
		for line in lines:
			height+=1
			pixels=pixels+line.split("\t")
		
		width=len(line.split("\t"))
		width=int(width)
		height=int(height)
		pixels=[float(x) for x in pixels]
		#print(width,height)
		return ImagePlus("imgFromtxt", FloatProcessor(width, height, pixels))
	
	def SubstractFromTxt(self,img,pixelData):
		pixelsRef = img.getProcessor().getPixels()
		pixelsRef=zip(pixelsRef)
		result=[]
		i=0
		for pixelRef in pixelsRef:
			result.append(pixelRef[0]-pixelData[i])
			i+=1
		return result
		
	def getStackNames(self,filePath,substring=""):
	#def getStackNames(self):
		#filePath="BAMRAW"
		allFiles=listdir(filePath)

		first=True
		if substring=="":
			result=allFiles
			for files in allFiles:
				imp=IJ.openImage(filePath+files)
				if first==True:
					impStack=ImageStack(imp.getProcessor().getWidth(),imp.getProcessor().getHeight())
					first=False
				
				impStack.addSlice(files,imp.getProcessor())
		else:
			result=[]
			
			for files in allFiles:
				#print(files)
				if substring in files:
					result.append(files)
					imp=IJ.openImage(filePath+files)
					if first==True:
						impStack=ImageStack(imp.getProcessor().getWidth(),imp.getProcessor().getHeight())
						first=False
					
					impStack.addSlice(files,imp.getProcessor())

	
		return result,impStack

	
	def StoreStatInArray(self,imgStackNames,path=""):
		resultMean=[]
		resultMax=[]
		resultMin=[]
		for name in imgStackNames:
			img=IJ.openImage(path+name)
			
			#result.append([img.getStatistics().mean,img.getStatistics().max,img.getStatistics().min])
			resultMean.append(img.getStatistics().mean)
			resultMax.append(img.getStatistics().max)
			resultMin.append(img.getStatistics().min)
		return [resultMean,resultMin,resultMax]
		
	def CalculatorArray(self,imgStackNames,vector,operation,path=""):
		'''
			Perform a operation of an array of values to each img of
			a stack

		'''

		if len(imgStackNames)!=len(vector):
			
			raise TypeError("Stack and vector must have the same length: %d vs %d" %(len(imgStackNames),+len(vector)))
		i=0
		firstIMG=IJ.openImage(path+imgStackNames[0])
		size=[firstIMG.getWidth(),firstIMG.getHeight()]
		myStack=ImageStack(size[0],size[1])
		for name in imgStackNames:
			img=IJ.openImage(path+name)
			img=self.ToUnsigned(img)
			pixels =img.getProcessor().getPixels()
			pixels=zip(pixels)
			minPixel=img.getStatistics().mean
			result=[]
			factor=-minPixel+vector[i]
			#print(vector[i],minPixel)
			#IJ.run("Calculator Plus", "i1=flat_4.jpg i2=Result2 operation=[Scale: i2 = i1 x k1 + k2] k1=1 k2=0 create");
			for pixel in pixels:
				result.append(pixel[0]+factor)
			resultFinal=ImagePlus('title', FloatProcessor(size[0], size[1], result))
			resultFinal=self.ToUnsigned(resultFinal)
			#result=IJ.run(img,"Macro", "code=v=v"+operation+str(vector[i])+"-"+str(minPixel)+";")
			#result=IJ.run(img,"Add..", "value=3;")
			#result.show()
			myStack.addSlice(name.replace(".jpg","_result.jpg"),resultFinal.getProcessor())
			i+=1
		return myStack
			
	def NormalizeIntensity(self,imgStackNames, BGStackNames,path=""):
	    #Get first image
	    
	    firstBG=IJ.openImage(path+BGStackNames[0])
	    lastBG=IJ.openImage(path+BGStackNames[-1])
	    #Get statistist
	    
	    refMinMaxOrig=[firstBG.getStatistics().mean,lastBG.getStatistics().mean]
	    print("First IMG: %s, Last IMG: %s" %(imgStackNames[0],imgStackNames[-1]))
	    print("First BG: %s, Last BG: %s" %(BGStackNames[0],BGStackNames[-1]))
	   
	    #Actually, I want first to be zero
	    refMinMax=[0,lastBG.getStatistics().mean]
	
	    #Get reference for each pixel from BG stack, from first and last BG at each step
	    firstBGPixels=zip(firstBG.getProcessor().getPixels())
	    lastBGixels=zip(lastBG.getProcessor().getPixels())
	    i=0
	    factor=[]
	    subtract=[]
	
	    size=[firstBG.getWidth(),firstBG.getHeight()]
	    #Create stack for save output
	    impStackOrig=ImageStack(size[0],size[1])
	    impStackResult=ImageStack(size[0],size[1])
	
	    for firstp in firstBGPixels:
	        lastp=lastBGixels[i]
	        try:
		        factor.append((refMinMax[1]-refMinMax[0])/(lastp[0]-firstp[0]))
		        subtract.append((-firstp[0])*factor[i]+refMinMax[0])
		        i+=1
	        except Exception,e:
		    	print(e,i)
		    	print(lastp[0],firstp[0])
		    	print(refMinMax[0],refMinMax[1])
		    	print(refMinMaxOrig[0],refMinMaxOrig[1])
		    	return
	    
	    i=0
	    for imgName in imgStackNames:
	        img=IJ.openImage(path+imgName)
	
	        j=0
	        #imgPixels=zip(img.getProcessor().getPixels())
	        result=[]
	        #result=IJ.run(imp,"Macro", "code=v=(v-%.4f)*%.4f+%.4f;" %(stackMinMax[0],factor,refMinMax[0]))
	        imgPixels=img.getProcessor().getPixels()
	        #pix2 = map(lambda x,f,sub: x[0] * f + sub, (imgPixels,factor,subtract)
	        
	        for pixel in imgPixels:
	            #result.append((pixel[0]-firstBGPixels[j][0])*factor[j]+refMinMax[0])
	            result.append(pixel[0]*factor[j]+subtract[j])
	            j+=1
	        
	        resultIMG= ImagePlus('title', FloatProcessor(size[0], size[1], result))
	        impStackOrig.addSlice(imgName,img.getProcessor())
	        impStackResult.addSlice(imgName.replace(".jpg","_result.jpg"),resultIMG.getProcessor())
	        i+=1
	    
	    return [impStackOrig,impStackResult]


