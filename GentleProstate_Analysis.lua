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

function clear()
  for i = 1, wm.scan.len do
    wm.scan[i]:clear()
  end
end

require ('csv')
folder = [[D:\data\PCUK\ALL_DATA\19-20_fractions\packs\]]
folderADMIRE = [[D:\data\ADMIRE2WMatch\inter\]]
patientList = readCSV([[D:\data\alex_tom\prostatePatient\new19_20_fracs_AM_20181024.csv]])

--------------------------------------------------------------------------------------------------------------------------------
-- iterate through the list of patients, open auto-contour, compare to doctors, calculate and export statistics for comparison
--------------------------------------------------------------------------------------------------------------------------------
for i =1, #patientList do 
   -- check the patient pack exists and correct according to our study (i.e. as shown in the CSV file)
  if (fileexists(folder..patientList[i].patientID..[[.pack]])) then
    print ("Processing patient "..patientList[i].patientID)
    loadpack(folder..patientList[i].patientID..[[.pack]]) 

    -- load autocontours onto loaded pack
    autocontour = Delineation:new()
    AVS:READ_XDR(autocontour.Dots, folderADMIRE..[[processedAlexAndTom\]]..patientList[i].patientID..[[.dwp]])
    AVS:READ_XDR(autocontour.Index, folderADMIRE..[[processedAlexAndTom\]]..patientList[i].patientID..[[.dwi]])
    AVS:READ_XDR(autocontour.Lut, folderADMIRE..[[processedAlexAndTom\]]..patientList[i].patientID..[[.dwl]])
    wm.Delineation = autocontour

    -- Open the contour and auto-contour in seperate scan windows
    wm.scan[3] = wm.scan[1]:burn (wm.Delineation.prostate)
    AVS:DIL_SET_NAME(wm.delineation.lut, wm.delineation.lut, 0, [[Prostate_STAPLE_ADMIRE]]) -- rename the delineation as poor format
    wm.scan[4] = wm.scan[1]:burn (wm.Delineation.Prostate_STAPLE_ADMIRE)
    ----------------------------------------------------------------------------
    -- calculates stats against the auto-contour and contour for each patient
    ----------------------------------------------------------------------------
    
    -- reference surface for analysis
    refDots = field:new()
    refIndex = field:new()
    AVS:FIELD_ISOSURFACE(wm.scan[4].data, refDots, refIndex, 50) -- still unsure on this functions purpose and AVS?
    
    -- perform distance to agreement calculation
    --AVS:READ_XDR(wm.scan[1].data, data..[[\]]..observer[i]..[[_]]..Visit..[[\Burns\]]..j..[[_]]..observer[i]..[[_]]..scanner[k]..[[.xdr]])
   -- wm.scan[1].data = wm.Delineation.prostate
    wm.scan[3] = wm.scan[3]*256 -- why *256?
    wm.scan[3].data:tofloat()

    testDots = field:new()
    testIndex = field:new()
    dist1 = field:new()
    dist2 = field:new()
    hist = field:new()

    -- converts contour to surface for comparison
    AVS:FIELD_ISOSURFACE(wm.scan[3].data, testDots, testIndex, 50)

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
    wm.scan[3].data:toshort()
    wm.scan[4].data:toshort()

    AVS:FIELD_AND(wm.scan[3].data, wm.scan[4].data, DSCtmp)
    wm.scan[5]:clear()
    wm.scan[5].data = DSCtmp

    DSC = (wm.scan[5]:volume().value*2)/(wm.scan[3]:volume().value+wm.scan[4]:volume().value)

    -- print results
    -- scanner, observer, mean DTA, SD DTA, volume, DSC 
    --print(scanner[k], observer[i], g_mean.value, g_sd.value, wm.scan[1]:volume().value, DSC)
  end
  collectgarbage()
end

print("Finish")
