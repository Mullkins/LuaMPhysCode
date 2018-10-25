-- A program which will quantify the uncertainty between our average doctors contour (RF-fusion ATLAS auto-contour) and a doctors contour of patients prostate.

function scandir(directory)
  -- A function which will scan the directory and return an array of constituent filenames
    local i, t, popen = 0, {}, io.popen
    for filename in popen('dir "'..directory..'" /o:n /b'):lines() do
        i = i + 1
        t[i] = filename
    end
    return t
end

require ('csv')
folder = [[D:\data\PCUK\ALL_DATA\19-20_fractions\packs\]]
folderADMIRE = [[D:\data\ADMIRE2WMatch\inter\]]
patientList = readCSV([[D:\data\alex_tom\prostatePatient\new19_20_fracs_AM_20181024.csv]])

-- iterate through the list of patients, open auto-contour, compare to doctors, calculate and export statistics for comparison
for i =1, #patientList do 
  print ("Processing patient "..patientList[i].ID)
  loadpack(folder..patientList[i].ID..[[.pack]]) 
  
  autocontour = Delineation:new()
  AVS:READ_XDR(a.Dots, folderADMIRE..[[processedAlexAndTom\]]..patientList[i].ID..[[.dwp]])
  AVS:READ_XDR(a.Index, folderADMIRE..[[processedAlexAndTom\]]..patientList[i].ID..[[.dwi]])
  AVS:READ_XDR(a.Lut, folderADMIRE..[[processedAlexAndTom\]]..patientList[i].ID..[[.dwl]])
  
  wm.Delineation = autocontour

  -- calculates stats against the median contour for each observer
  -- reloads into scan 1 each oberver
  for i = 1, #observer do
    -- Perform distance to agreement calculation
    if fileexists(data..[[\]]..observer[i]..[[_]]..Visit..[[\Burns\]]..j..[[_]]..observer[i]..[[_]]..scanner[k]..[[.xdr]]) then
      AVS:READ_XDR(wm.scan[1].data, data..[[\]]..observer[i]..[[_]]..Visit..[[\Burns\]]..j..[[_]]..observer[i]..[[_]]..scanner[k]..[[.xdr]])
      wm.scan[1] = wm.scan[1]*256
      wm.scan[1].data:tofloat()
      
      testDots = field:new()
      testIndex = field:new()
      dist1 = field:new()
      dist2 = field:new()
      hist = field:new()
      
      -- converts contour to surface for comparison
      AVS:FIELD_ISOSURFACE(wm.scan[1].data, testDots, testIndex, 128)
      
      -- perfoms a surface distance calculation and converts to a histogram
      AVS:SURF_DIST(refDots, refIndex, testDots, testIndex, dist1)
      --AVS:SURF_DIST(testDots, testIndex, refDots, refIndex, dist2)
      --dist1:concat(dist2, 1)
      
      -- performs stats
      AVS:FIELD_HIST(dist1, hist, 0, 0, 256)
      g_mean = field:new()
      AVS:HISTOGRAM_STAT(hist,g_mean,3)  -- mean DTA
      g_sd = field:new()
      AVS:HISTOGRAM_STAT(hist,g_sd,4)  -- SD of DTA
      --hist:plot()
              
      -- Calculated the DSC
      DSC = 0
      DSCtmp = field:new()
      wm.scan[1].data:toshort()
      wm.scan[2].data:toshort()
      
      AVS:FIELD_AND(wm.scan[1].data, wm.scan[2].data, DSCtmp)
      wm.scan[5]:clear()
      wm.scan[5].data = DSCtmp
              
      DSC = (wm.scan[5]:volume().value*2)/(wm.scan[1]:volume().value+wm.scan[2]:volume().value)
             
      -- print results
      -- scanner, observer, mean DTA, SD DTA, volume, DSC 
      print(scanner[k], observer[i], g_mean.value, g_sd.value, wm.scan[1]:volume().value, DSC)
    end
  end
  collectgarbage()
end

print("Finish")
