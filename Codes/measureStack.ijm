
//
// This macro measure all the slices in a stack.
name="Stack"
selectWindow(name);
run("Select None");
makeRectangle(160, 98, 66, 48);
//makePoint(518, 58, "small yellow hybrid");
//makePoint(505, 222, "small yellow hybrid");
/*
  macro "Measure Stack" {
       saveSettings;
       setOption("Stack position", true);
       for (n=1; n<=nSlices; n++) {
          setSlice(n);
          run("Measure");
      }
      restoreSettings;
  }
*/
run("Plot Z-axis Profile");

selectWindow(name);
run("Select None");
makeRectangle(557, 24, 67, 55);
//makePoint(116, 57, "small yellow hybrid");
run("Plot Z-axis Profile");


selectWindow(name);
run("Select None");
makeRectangle(323, 263, 69, 56);
//makePoint(342, 206, "small yellow hybrid");
run("Plot Z-axis Profile");


Plot.addFromPlot(name+"-160-98", 0);
Plot.setStyle(0, "blue,none,1.0,Line");
Plot.addFromPlot(name+"-557-24", 0);
Plot.setStyle(1, "red,none,1.0,Line");
