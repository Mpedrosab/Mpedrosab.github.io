//run("Analyze Particles...", "size=5-Infinity show=Masks display clear in_situ stack");
run("Calculator Plus", "i1=BAMRAW-1 i2=BAMRAW-4 operation=[Subtract: i2 = (i1-i2) x k1 + k2] k1=1 k2=0 create");
for (n=1; n<=nSlices; n++) {
  setSlice(n);
//setThreshold(20, 255);
run("Create Selection");
roiManager("Add");
}

waitForUser("open your second stack");

r = roiManager("count");
 for (i=r-1; i>=0; i--) {
roiManager("select", i);
     roiManager("Measure");
run("Set...", "value=NaN");
}


//Add mean of other stack to this stack
selectWindow("Result");
for (n=1; n<=nSlices; n++) {

selectWindow("FitResult");
  setSlice(n);
  intensFit = getValue("Mean");
selectWindow("Result");
setSlice(n);
  intensIn= getValue("Mean");
run("Add...", "value="+intensFit);
  intensOut = getValue("Mean");
  print("Before,Fit,Result:",intensIn,intensFit,intensOut);
}
