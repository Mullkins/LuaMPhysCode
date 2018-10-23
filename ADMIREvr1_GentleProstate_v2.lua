
function scandir(directory)
    local i, t, popen = 0, {}, io.popen
    for filename in popen('dir "'..directory..'" /o:n /b'):lines() do
        i = i + 1
        t[i] = filename
    end
    return t
end

function clear()
  wm.Delineation:clear()
  for i = 1, wm.scan.len do
    wm.scan[i]:clear()
  end
end
 
function QCimage()
 -- save a screen shot for checking
  setpage(3)
  wm.View.Slice = 256
  snapshot(folderADMIRE..[[qaAlexAndTom\]]..patientList[i]..[[.jpg]])
end

function GetFileName(url)
  -- returns the file name without the extension
  return url:match("[^/]-([^.]+)")
end

require ('csv')
folder = [[D:\data\alex_tom\prostate_packs\]]
folderADMIRE = [[D:\data\ADMIRE2WMatch\inter\]]

takeQCimage = false

patientList = scandir(folder) -- array of pack names


for i =1, #patientList do --#patientList do
  -- Reformat the string i.e. XXXXX.pack, into XXXX to be saved correctly as different formats
  patientName = {}
  patientName = GetFileName(patientList[i])
   
  if not fileexists(folderADMIRE..[[processedAlexAndTom\]]..patientName[i]) then
    print (i.." Processing patient "..patientName[i])
 
    -- load dummy DICOM to create header file
    wm.scan[3]:load([[DCM:D:\data\ADMIRE2WMatch\dummyDicom\1.3.6.1.4.1.32722.107512530760489863685055474273076483714.dcm]])
    
    -- making folders in the current folderADMIRE directory i.e. [D:\data\ADMIRE2WMatch\inter\]
    os.execute('mkdir '..folderADMIRE..[[tmpDataAlexAndTom]])
    os.execute('mkdir '..folderADMIRE..[[ResultsAlexAndTom]])
    os.execute('mkdir '..folderADMIRE..[[qaAlexAndTom]])
    os.execute('mkdir '..folderADMIRE..[[processedAlexAndTom]])
    
    -- copy folder to the other directory stated
    os.execute('cp '..folderADMIRE..[[\..\.file_1 C:\ProgramData\ADMIRE]])
    os.execute('cp '..folderADMIRE..[[\..\.file_2 C:\ProgramData\ADMIRE]])
    
    -- export DICOM and run ADMIRE.  Expects patient to be in a folder called tmpData and will return results to a folder called Results
    wm.scan[1]:export(folderADMIRE..[[tmpDataAlexAndTom\%d.dcm]], wm.scan[3].properties)  --move properties of scan 3 from tmpData folder to scan 1
    os.execute(folderADMIRE..[[Batch_GentleProstate_2atlases.bat]]) -- run the batch
    
    -- rename the structure file to remove square brackets and loads new structures
    t = {} -- initialise t
    t = scandir(folderADMIRE..[[ResultsAlexAndTom\]]) -- t = an array of file names (strings) in D:\data\ADMIRE2WMatch\inter\Results\
    --os.rename(folderADMIRE..[[ResultsAlexAndTom\]]..[[09_20180917T111132[GENRF]_816917893_RTS]], folderADMIRE..[[ResultsAlexAndTom\]]..[[ struct.dcm]])
    os.execute('rename '..folderADMIRE..[[ResultsAlexAndTom\]]..t[1]..[[ struct.dcm]])  -- renames element t[1] as struct.dcm 
    
    -- store the previous delineations as 'a'
    a = Delineation:new()
    a:assign(wm.Delineation)
    
    -- load and combine all delineations
    wm.Delineation:load(folderADMIRE .. [[ResultsAlexAndTom\struct.dcm]], wm.Scan[3]) -- loads wm.scan[3] from struct.dcm
    for j = 1, wm.delineation.len do -- loop through total list of delineations 
      tmp = wm.delineation[j-1].name -- save each name as tmp (temporary name)
      AVS:DIL_SET_NAME(wm.delineation.lut, wm.delineation.lut, j-1, tmp..[[_ADMIRE]]) -- set the name of the delineation, lup = look up table
    end
    AVS:DIL_ADD(wm.Delineation.Dots, wm.Delineation.Index, wm.Delineation.Lut, a.Dots, a.Index, a.Lut, wm.Delineation.Dots, wm.Delineation.Index, wm.Delineation.Lut) -- combine all
   
    -- Save contours  
    -- AVS:WRITE_XDR(wm.Delineation.Dots, folderADMIRE..[[processedAlexAndTom\]]..patientName..[[.dwp]])
    -- AVS:WRITE_XDR(wm.Delineation.Index, folderADMIRE..[[processedAlexAndTom\]]..patientName..[[.dwi]])
    -- AVS:WRITE_XDR(wm.Delineation.Lut, folderADMIRE..[[processedAlexAndTom\]]..patientName..[[.dwl]])
    
    --Save as pack (larger)
    wm.scan[3]:clear()
    savepack(folderADMIRE..[[processedAlexAndTom\]]..patientList[i])

    -- clear data from run
    t = {}
    t = scandir(folderADMIRE..[[tmpDataAlexAndTom]])
    for j = 1, #t do
      os.remove(folderADMIRE..[[tmpDataAlexAndTom\]]..t[j])
    end
    os.remove(folderADMIRE..[[ResultsAlexAndTom\struct.dcm]])
    
    --[[if takeQCimage == true then
      QCimage() 
    end]]
    
    clear()
    collectgarbage()
  end
end

print("Finish")
