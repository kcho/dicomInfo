#!/ccnc_bin/venv/bin/python2.7
__authors__=['Kevin','Takwan','BeumJun']

import textwrap
import dicom
import re
import os
import sys
import argparse
from inspect import ismethod

infoList = ['AccessionNumber', 'AcquisitionDate', 'AcquisitionMatrix', 'AcquisitionNumber', 'AcquisitionTime', 'AngioFlag', 'BitsAllocated', 'BitsStored', 'Columns', 'ContentDate', 'ContentTime', 'DeviceSerialNumber', 'EchoNumbers', 'EchoTime', 'EchoTrainLength', 'FlipAngle', 'FrameOfReferenceUID', 'HighBit', 'ImageOrientationPatient', 'ImagePositionPatient', 'ImageType', 'ImagedNucleus', 'ImagingFrequency', 'InPlanePhaseEncodingDirection', 'InstanceCreationDate', 'InstanceCreationTime', 'InstanceNumber', 'InstitutionAddress', 'InstitutionName', 'InstitutionalDepartmentName', 'LargestImagePixelValue', 'MRAcquisitionType', 'MagneticFieldStrength', 'Manufacturer', 'ManufacturerModelName', 'Modality', 'NumberOfAverages', 'NumberOfPhaseEncodingSteps', 'OperatorsName', 'PatientAge', 'PatientBirthDate', 'PatientID', 'PatientName', 'PatientPosition', 'PatientSex', 'PatientWeight', 'PercentPhaseFieldOfView', 'PercentSampling', 'PerformedProcedureStepDescription', 'PerformedProcedureStepID', 'PerformedProcedureStepStartDate', 'PerformedProcedureStepStartTime', 'PerformingPhysicianName', 'PhotometricInterpretation', 'PhysiciansOfRecord', 'PixelBandwidth', 'PixelData', 'PixelRepresentation', 'PixelSpacing', 'PositionReferenceIndicator', 'ProtocolName', 'RefdImageSequence', 'ReferencedImageSequence', 'ReferringPhysicianName', 'RepetitionTime', 'RequestAttributesSequence', 'RequestedProcedureDescription', 'RequestingPhysician', 'Rows', 'SAR', 'SOPClassUID', 'SOPInstanceUID', 'SamplesPerPixel', 'ScanOptions', 'ScanningSequence', 'SequenceName', 'SequenceVariant', 'SeriesDate', 'SeriesDescription', 'SeriesInstanceUID', 'SeriesNumber', 'SeriesTime', 'SliceLocation', 'SliceThickness', 'SmallestImagePixelValue', 'SoftwareVersions', 'SpacingBetweenSlices', 'StationName', 'StudyDate', 'StudyDescription', 'StudyID', 'StudyInstanceUID', 'StudyTime', 'TransmitCoilName', 'VariableFlipAngleFlag']

# In[83]:

def getDicomInfo(directory):
    '''
    Input : directory location
    Output : dicom information
    '''

    #Looping through the input directory
    switch='non-break'
    firstDicomFile=''

    for root, dirs, files in os.walk(directory):
        try: 
            dicomFiles = [x for x in files if re.search('.*ima|.*dcm|\d{8}',x)]
            firstDicomFile = dicomFiles[0]

            try:
                firstDicomInfo = dicom.read_file(os.path.join(root,firstDicomFile))
            except:
                firstDicomInfo = dicom.read_file(os.path.join(root,firstDicomFile), force=True)

            return firstDicomInfo
        except:
            pass

        ##Looping through the bunch of files
        #for singleFile in files:

            ##if there is dicom files
            #if re.search('.*ima|.*dcm|\d{8}',singleFile,flags=re.IGNORECASE):
                #try:
                    #firstDicomFile = dicom.read_file(os.path.join(root,singleFile))
                #except:
                    #firstDicomFile = dicom.read_file(os.path.join(root,singleFile),force=True)

                ##make a switch to turn off the later loops
                #switch='break'

                ##turn the file loop off
                #break
            #else:
                #switch='non-break'

        ##if switch is on, turn the dir loop off
        #if switch=='break':
            #break


def getDicomInfo2(dicomFile):
    try:
        firstDicomInfo = dicom.read_file(dicomFile)
    except:
        firstDicomInfo = dicom.read_file(dicomFile,force=True)
    return firstDicomInfo

def main(args):
    if args.dicom == None:
        firstDicomInfo = getDicomInfo(args.directory)
    else:
        firstDicomInfo = getDicomInfo2(args.dicom)

    if args.option == None:
        print firstDicomInfo
    else:
        for option in args.option:
            attribute = getattr(firstDicomInfo, option)
            print attribute

   
   # if response == 'AccessionNumber':
   #     print firstDicomFile.AccessionNumber
   # if response == 'AcquisitionDate':
   #     print firstDicomFile.AcquisitionDate
   # if response == 'PatientName':
   #     print firstDicomFile.PatientName


    #if args.accessionnumber:
        #print firstdicomfile.accessionnumber
    #if args.patientname:
        #print 'patient name:',firstdicomfile.patientname
    #if args.acquisitiondate:
        #print 'acquisition date:',firstdicomfile.acquisitiondate
    #if args.acquisitionmatrix:
        #print 'acquisition matrix:',firstdicomfile.acquisitionmatrix
    #if args.acquisitionnumber:
        #print 'acquisition number:',firstdicomfile.acquisitionnumber
    #if args.acquisitiontime:
        #print 'acquisition time:',firstdicomfile.aquisitiontime
    #if args.angioflag:
        #print 'angio flag:',firstdicomfile.angioflag
    #if args.bitsallocated:
        #print 'bits allocated:',firstdicomfile.bitsallocated
    #if args.bitsstored:
        #print 'bits stored:',firstdicomfile.bitsstored
    #if args.columns:
        #print 'columns:',firstdicomfile.columns
    #if args.contentdate:
        #print 'content date:',firstdicomfile.contentdate
    #if args.contenttime:
        #print 'content time:',firstdicomfile.contenttime
    #if args.deviceserialnumber:
        #print 'device serial number:',firstdicomfile.deviceserialnumber
    #if args.echonumbers:
        #print 'echo numbers:',firstdicomfile.echonumbers
    #if args.echotime:
        #print 'echo time:',firstdicomfile.echotime
    #if args.echotrainlength:
        #print 'echo train length:',firstdicomfile.echotrainlength
    #if args.flipangle:
        #print 'flip angle:',firstdicomfile.flipangle
    #if args.frameofreferenceuid:
        #print 'frame of reference uid:',firstdicomfile.frameofreferenceuid
    #if args.highbit:
        #print 'high bit:',firstdicomfile.highbit
    #if args.imageorientationpatient:
        #print 'image oreigntation patient:',firstdicomfile.imageorientationpatient
    #if args.imagepositionpatient:
        #print 'image position patient:',firstdicomfile.imagepositionpatient
    #if args.imagetype:
        #print 'image type:',firstdicomfile.imagetype
    #if args.imagednucleus:
        #print 'imaged nucleus:',firstdicomfile.imagednucleus
    #if args.imagingfrequency:
        #print 'imaging frequency:',firstdicomfile.imagingfrequency
    #if args.inplanephaseencodingdirection:
        #print 'in plane phase encoding direction:',firstdicomfile.inplanephaseencodingdirection
    #if args.instancecreationdate:
        #print 'instance creation date:',firstdicomfile.instancecreationdate
    #if args.instancenumber:
        #print 'instance number:',firstdicomfile.instancenumber
    #if args.institutionaddress:
        #print 'institution address:',firstdicomfile.institutionaddress
    #if args.institutionname:
        #print 'institution name:',firstdicomfile.institutionname
    #if args.institutionaldepartmentname:
        #print 'institutional department name:',firstdicomfile.institutionaldepartmentname
    #if args.largestimagepixelvalue:
        #print 'largest image pixel value:',firstdicomfile.largestimagepixelvalue
    #if args.mracquisitiontype:
        #print 'mr acquisition type:',firstdicomfile.mracquisitiontype
    #if args.magneticfieldstrength: 
        #print 'magnetic field strength:',firstdicomfile.magneticfieldstrength
    #if args.manufacturer:
        #print 'manufacturer:',firstdicomfile.manufacturer
    #if args.manufacturermodelname:
        #print 'manufacturer model name:',firstdicomfile.manufacturermodelname
    #if args.modality:
        #print 'modality:',firstdicomfile.modality
    #if args.numberofaverages:
        #print 'number of averages:',firstdicomfile.numberofaverages
    #if args.numberofphaseencodingsteps:
        #print 'number of phase encoding steps:',firstdicomfile.numberofphaseencodingsteps
    #if args.operatorsname:
        #print 'operators name:',firstdicomfile.operatorsname
    #if args.patientage:
        #print 'patient age:',firstdicomfile.patientage
    #if args.patientbirthdate:
        #print 'patient birth date:',firstdicomfile.patientbirthdate
    #if args.patientid:
        #print 'patient id:',firstdicomfile.patientid
    #if args.patientposition:
        #print 'patient position:',firstdicomfile.patientposition
    #if args.patientsex:
        #print 'patient sex:',firstdicomfile.patientsex
    #if args.patientweight:
        #print 'patient weight:',firstdicomfile.patientweight
    #if args.percentphasefieldofview:
        #print 'percent phase field of view:',firstdicomfile.percentphasefieldofview
    #if args.percentsampling:
        #print 'percent sampling:',firstdicomfile.percentsampling
    #if args.performedprocedurestepdescription:
        #print 'performed procedure step description:',firstdicomfile.performedprocedurestepdescription
    #if args.performedprocedurestepid:
        #print 'performed procedure step id:',firstdicomfile.performedprocedurestepid
    #if args.performedprocedurestepstartdate:
        #print 'performed procedure step start date:',firstdicomfile.performedprocedurestepstartdate
    #if args.performedprocedurestepstarttime:
        #print 'performed procedure step start time:',firstdicomfile.performedprocedurestepstarttime
    #if args.performingphysicianname:
        #print 'performing physician name:',firstdicomfile.performingphysicianname
    #if args.photometricinterpretation:
        #print 'photometric interpretation:',firstdicomfile.photometricinterpretation
    #if args.physiciansofrecord:
        #print 'physicians of record:',firstdicomfile.physiciansofrecord
    #if args.pixelbandwidth:
        #print 'pixel bandwidth:',firstdicomfile.pixelbandwidth
    #if args.pixeldata:
        #print 'pixel data:',firstdicomfile.pixeldata
    #if args.pixelrepresentation:
        #print 'pixel representation:',firstdicomfile.pixelrepresentation
    #if args.pixelspacing:
        #print 'pixel spacing:',firstdicomfile.pixelspacing
    #if args.positionreferenceindicator:
        #print 'position reference indicator:',firstdicomfile.positionreferenceindicator
    #if args.protocolname:
        #print 'protocol name:',firstdicomfile.protocolname
    #if args.refdimagesequence:
        #print 'refd image sequence:',firstdicomfile.refdimagesequence
    #if args.referencedimagesequence:
        #print 'referenced image sequence:',firstdicomfile.referencedimagesequence
    #if args.referringphysicianname:
        #print 'referring physician name:',firstdicomfile.referringphysicianname
    #if args.repetitiontime:
        #print 'repetition time:',firstdicomfile.repetitiontime
    #if args.requestattributessequence:
        #print 'request attributes sequence:',firstdicomfile.requestsattributesequence
    #if args.requestedproceduredescription:
        #print 'requested procedure description:',firstdicomfile.requestedproceduredescription
    #if args.requestingphysician:
        #print 'requesting physician:',firstdicomfile.requestingphysician
    #if args.rows:
        #print 'rows:',firstdicomfile.rows
    #if args.sar:
        #print 'sar:',firstdicomfile.sar
    #if args.sopclassuid:
        #print 'sop class uid:',firstdicomfile.sopclassuid
    #if args.sopinstanceuid:
        #print 'sop instance uid:',firstdicomfile.sopinstanceuid
    #if args.samplesperpixel:
        #print 'samples per pixel:',firstdicomfile.samplesperpixel
    #if args.scanoptions:
        #print 'scan options:',firstdicomfile.scanoptions
    #if args.scanningsequence:
        #print 'scanning sequence:',firstdicomfile.scanningsequence
    #if args.sequencename:
        #print 'sequence name:',firstdicomfile.sequencename
    #if args.sequencevariant:
        #print 'sequence variant:',firstdicomfile.sequencevariant
    #if args.seriesdate:
        #print 'series date:',firstdicomfile.seriesdate
    #if args.seriesdescription:
        #print 'series description:',firstdicomfile.seriesdescription
    #if args.seriesinstanceuid:
        #print 'series instance uid:',firstdicomfile.seriesinstanceuid
    #if args.seriesnumber:
        #print 'series number:',firstdicomfile.seriesnumber
    #if args.seriestime:
        #print 'series time:',firstdicomfile.seriestime
    #if args.slicelocation:
        #print 'slice location:',firstdicomfile.slicelocation
    #if args.slicethickness:
        #print 'slice thickness:',firstdicomfile.slicethickness
    #if args.smallestimagepixelvalue:
        #print 'smallest image pixel value:',firstdicomfile.smallestimagepixelvalue
    #if args.softwareversions:
        #print 'software versions:',firstdicomfile.softwareversions
    #if args.spacingbetweenslices:
        #print 'spacing between slices:',firstdicomfile.spacingbetweenslices
    #if args.stationname:
        #print 'station name:',firstdicomfile.stationname
    #if args.studydate:
        #print 'study date:',firstdicomfile.studydate
    #if args.studydescription:
        #print 'study description:',firstdicomfile.studydescription
    #if args.studyid:
        #print 'study id:',firstdicomfile.studyid
    #if args.studyinstanceuid:
        #print 'study instance uid:',firstdicomfile.studyinstanceuid
    #if args.studytime:
        #print 'study time:',firstdicomfile.studparserytime
    #if args.transmitcoilname:
        #print 'transmit coil name:',firstdicomfile.transmitcoilname
    #if args.variableflipangleflag:
        #print 'variable flip angle flag:',firstdicomfile.variableflipangleflag
    #if args.windowcenter:
        #print 'window center:',firstdicomfile.windowcenter
    #if args.windowcenterwidthexplanation:
        #print 'window center width explanation:',firstdicomfile.windowcenterwidthexplanation


    


           #parser.add_argument('-t','--tak',action='store_true',help="print tak's information")

  #  except:
        #print re.findall('\x08\x00(\d{8})\x10\x00',' '.join(firstdicomfile.mediastoragesopclassuid[5])),
        #print re.findall('\x08\x00(\d{8})\x10\x00',' '.join(firstdicomfile.mediastoragesopclassuid[6]))

       # print firstdicomfile
  #      print 'data displayed'

        #four = re.findall('\x08\x00(\d{8})\x10\x00',firstdicomfile.mediastoragesopclassuid[4])
        #five = re.findall('\x08\x00(\d{8})\x10\x00',firstdicomfile.mediastoragesopclassuid[5])
        #six = re.findall('\x08\x00(\d{8})\x10\x00',firstdicomfile.mediastoragesopclassuid[6])

        #if four != []:
            #print four
        #elif five != []:
            #print five
        #else:
            #print six



if __name__=='__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description = textwrap.dedent('''\
                    {codeName} : Returns information extracted from dicom within the directory
                    ====================
                        eg) {codeName}
                        eg) {codeName} -dir /Users/kevin/NOR04_CKI -o PatientID PatientName

                    options: 
                    {infoList}
                    '''.format(codeName=os.path.basename(__file__),
                        infoList=', '.join(infoList))))

            #epilog="By Kevin, 26th May 2014")

    parser.add_argument("-dir","--directory",help="Data directory location, default = pwd",default=os.getcwd())
    parser.add_argument("-dic","--dicom",help="Dicom location")
    parser.add_argument("-o","--option",nargs='+',help="Information to print. Choose from the options above")

    args = parser.parse_args()

    main(args)


#    parser.add_argument("-AccessionNumber","--AccessionNumber",action="store_true",help="Get AccessionNumber")
#    parser.add_argument("-AcquisitionDate","--AcquisitionDate",action="store_true",help="Get AcquisitionDate")
#    parser.add_argument("-AcquisitionMatrix","--AcquisitionMatrix",action="store_true",help="Get AcquisitionMatrix")
#    parser.add_argument("-AcquisitionNumber","--AcquisitionNumber",action="store_true",help="Get AcquisitionNumber")
#    parser.add_argument("-AcquisitionTime","--AcquisitionTime",action="store_true",help="Get AcquisitionTime")
#    parser.add_argument("-AngioFlag","--AngioFlag",action="store_true",help="Get AngioFlag")
#    parser.add_argument("-BitsAllocated","--BitsAllocated",action="store_true",help="Get BitsAllocated")
#    parser.add_argument("-BitsStored","--BitsStored",action="store_true",help="Get BitsStored")
#    parser.add_argument("-Columns","--Columns",action="store_true",help="Get Columns")
#    parser.add_argument("-ContentDate","--ContentDate",action="store_true",help="Get ContentDate")
#    parser.add_argument("-ContentTime","--ContentTime",action="store_true",help="Get ContentTime")
#    parser.add_argument("-DeviceSerialNumber","--DeviceSerialNumber",action="store_true",help="Get DeviceSerialNumber")
#    parser.add_argument("-EchoNumbers","--EchoNumbers",action="store_true",help="Get EchoNumbers")
#    parser.add_argument("-EchoTime","--EchoTime",action="store_true",help="Get EchoTime")
#    parser.add_argument("-EchoTrainLength","--EchoTrainLength",action="store_true",help="Get EchoTrainLength")
#    parser.add_argument("-FlipAngle","--FlipAngle",action="store_true",help="Get FlipAngle")
#    parser.add_argument("-FrameOfReferenceUID","--FrameOfReferenceUID",action="store_true",help="Get FrameOfReferenceUID")
#    parser.add_argument("-HighBit","--HighBit",action="store_true",help="Get HighBit")
#    parser.add_argument("-ImageOrientationPatient","--ImageOrientationPatient",action="store_true",help="Get ImageOrientationPatient")
#    parser.add_argument("-ImagePositionPatient","--ImagePositionPatient",action="store_true",help="Get ImagePositionPatient")
#    parser.add_argument("-ImageType","--ImageType",action="store_true",help="Get ImageType")
#    parser.add_argument("-ImagedNucleus","--ImagedNucleus",action="store_true",help="Get ImagedNucleus")
#    parser.add_argument("-ImagingFrequency","--ImagingFrequency",action="store_true",help="Get ImagingFrequency")
#    parser.add_argument("-InPlanePhaseEncodingDirection","--InPlanePhaseEncodingDirection",action="store_true",help="Get InPlanePhaseEncodingDirection")
#    parser.add_argument("-InstanceCreationDate","--InstanceCreationDate",action="store_true",help="Get InstanceCreationDate")
#    parser.add_argument("-InstanceCreationTime","--InstanceCreationTime",action="store_true",help="Get InstanceCreationTime")
#    parser.add_argument("-InstanceNumber","--InstanceNumber",action="store_true",help="Get InstanceNumber")
#    parser.add_argument("-InstitutionAddress","--InstitutionAddress",action="store_true",help="Get InstitutionAddress")
#    parser.add_argument("-InstitutionName","--InstitutionName",action="store_true",help="Get InstitutionName")
#    parser.add_argument("-InstitutionalDepartmentName","--InstitutionalDepartmentName",action="store_true",help="Get InstitutionalDepartmentName")    
#    parser.add_argument("-LargestImagePixelValue","--LargestImagePixelValue",action="store_true",help="Get LargestImagePixelValue")                                        
#    parser.add_argument("-MRAcquisitionType","--MRAcquisitionType",action="store_true",help="Get MRAcquisitionType")                                                       
#    parser.add_argument("-MagneticFieldStrength","--MagneticFieldStrength",action="store_true",help="Get MagneticFieldStrength")                                           
#    parser.add_argument("-Manufacturer","--Manufacturer",action="store_true",help="Get Manufacturer")                                                                      
#    parser.add_argument("-ManufacturerModelName","--ManufacturerModelName",action="store_true",help="Get ManufacturerModelName")                                           
#    parser.add_argument("-Modality","--Modality",action="store_true",help="Get Modality")                                                                                  
#    parser.add_argument("-NumberOfAverages","--NumberOfAverages",action="store_true",help="Get NumberOfAverages")                                                          
#    parser.add_argument("-NumberOfPhaseEncodingSteps","--NumberOfPhaseEncodingSteps",action="store_true",help="Get NumberOfPhaseEncodingSteps")     
#    parser.add_argument("-OperatorsName","--OperatorsName",action="store_true",help="Get OperatorsName")                                                                   
#    parser.add_argument("-PatientAge","--PatientAge",action="store_true",help="Get PatientAge")                                                                            
#    parser.add_argument("-PatientBirthDate","--PatientBirthDate",action="store_true",help="Get PatientBirthDate")                                                          
#    parser.add_argument("-PatientID","--PatientID",action="store_true",help="Get PatientID")                                                                               
#    parser.add_argument("-PatientName","--PatientName",action="store_true",help="Get PatientName")                                                                         
#    parser.add_argument("-PatientPosition","--PatientPosition",action="store_true",help="Get PatientPosition")                                                             
#    parser.add_argument("-PatientSex","--PatientSex",action="store_true",help="Get PatientSex")                                                                            
#    parser.add_argument("-PatientWeight","--PatientWeight",action="store_true",help="Get PatientWeight")                                                                   
#    parser.add_argument("-PercentPhaseFieldOfView","--PercentPhaseFieldOfView",action="store_true",help="Get PercentPhaseFieldOfView")                                     
#    parser.add_argument("-PercentSampling","--PercentSampling",action="store_true",help="Get PercentSampling")                                                             
#    parser.add_argument("-PerformedProcedureStepDescription","--PerformedProcedureStepDescription",action="store_true",help="Get PerformedProcedureStepDescription")
#    parser.add_argument("-PerformedProcedureStepID","--PerformedProcedureStepID",action="store_true",help="Get PerformedProcedureStepID")                                  
#    parser.add_argument("-PerformedProcedureStepStartDate","--PerformedProcedureStepStartDate",action="store_true",help="Get PerformedProcedureStepStartDate")
#    parser.add_argument("-PerformedProcedureStepStartTime","--PerformedProcedureStepStartTime",action="store_true",help="Get PerformedProcedureStepStartTime")
#    parser.add_argument("-PerformingPhysicianName","--PerformingPhysicianName",action="store_true",help="Get PerformingPhysicianName")                                 
#    parser.add_argument("-PhotometricInterpretation","--PhotometricInterpretation",action="store_true",help="Get PhotometricInterpretation")  
#    parser.add_argument("-PhysiciansOfRecord","--PhysiciansOfRecord",action="store_true",help="Get PhysiciansOfRecord")                                                
#    parser.add_argument("-PixelBandwidth","--PixelBandwidth",action="store_true",help="Get PixelBandwidth")                                                            
#    parser.add_argument("-PixelData","--PixelData",action="store_true",help="Get PixelData")                                                                           
#    parser.add_argument("-PixelRepresentation","--PixelRepresentation",action="store_true",help="Get PixelRepresentation")                                             
#    parser.add_argument("-PixelSpacing","--PixelSpacing",action="store_true",help="Get PixelSpacing")                                                                  
#    parser.add_argument("-PositionReferenceIndicator","--PositionReferenceIndicator",action="store_true",help="Get PositionReferenceIndicator") 
#    parser.add_argument("-ProtocolName","--ProtocolName",action="store_true",help="Get ProtocolName")                                                                  
#    parser.add_argument("-RefdImageSequence","--RefdImageSequence",action="store_true",help="Get RefdImageSequence")                                                   
#    parser.add_argument("-ReferencedImageSequence","--ReferencedImageSequence",action="store_true",help="Get ReferencedImageSequence")                                 
#    parser.add_argument("-ReferringPhysicianName","--ReferringPhysicianName",action="store_true",help="Get ReferringPhysicianName")                                    
#    parser.add_argument("-RepetitionTime","--RepetitionTime",action="store_true",help="Get RepetitionTime")                                                            
#    parser.add_argument("-RequestAttributesSequence","--RequestAttributesSequence",action="store_true",help="Get RequestAttributesSequence")  
#    parser.add_argument("-RequestedProcedureDescription","--RequestedProcedureDescription",action="store_true",help="Get RequestedProcedureDescription")
#    parser.add_argument("-RequestingPhysician","--RequestingPhysician",action="store_true",help="Get RequestingPhysician")                                             
#    parser.add_argument("-Rows","--Rows",action="store_true",help="Get Rows")                                                                                          
#    parser.add_argument("-SAR","--SAR",action="store_true",help="Get SAR")                                                                                             
#    parser.add_argument("-SOPClassUID","--SOPClassUID",action="store_true",help="Get SOPClassUID")                                                                     
#    parser.add_argument("-SOPInstanceUID","--SOPInstanceUID",action="store_true",help="Get SOPInstanceUID")                                                            
#    parser.add_argument("-SamplesPerPixel","--SamplesPerPixel",action="store_true",help="Get SamplesPerPixel")                                                         
#    parser.add_argument("-ScanOptions","--ScanOptions",action="store_true",help="Get ScanOptions")                                                                     
#    parser.add_argument("-ScanningSequence","--ScanningSequence",action="store_true",help="Get ScanningSequence")                                                      
#    parser.add_argument("-SequenceName","--SequenceName",action="store_true",help="Get SequenceName")                                                                  
#    parser.add_argument("-SequenceVariant","--SequenceVariant",action="store_true",help="Get SequenceVariant")                                                         
#    parser.add_argument("-SeriesDate","--SeriesDate",action="store_true",help="Get SeriesDate")                                                                        
#    parser.add_argument("-SeriesDescription","--SeriesDescription",action="store_true",help="Get SeriesDescription")                                                   
#    parser.add_argument("-SeriesInstanceUID","--SeriesInstanceUID",action="store_true",help="Get SeriesInstanceUID")                                                   
#    parser.add_argument("-SeriesNumber","--SeriesNumber",action="store_true",help="Get SeriesNumber")                                                                  
#    parser.add_argument("-SeriesTime","--SeriesTime",action="store_true",help="Get SeriesTime")                                                                        
#    parser.add_argument("-SliceLocation","--SliceLocation",action="store_true",help="Get SliceLocation")                                                               
#    parser.add_argument("-SliceThickness","--SliceThickness",action="store_true",help="Get SliceThickness")                                                            
#    parser.add_argument("-SmallestImagePixelValue","--SmallestImagePixelValue",action="store_true",help="Get SmallestImagePixelValue")                                 
#    parser.add_argument("-SoftwareVersions","--SoftwareVersions",action="store_true",help="Get SoftwareVersions")                                                      
#    parser.add_argument("-SpacingBetweenSlices","--SpacingBetweenSlices",action="store_true",help="Get SpacingBetweenSlices")                                          
#    parser.add_argument("-StationName","--StationName",action="store_true",help="Get StationName")                                                                     
#    parser.add_argument("-StudyDate","--StudyDate",action="store_true",help="Get StudyDate")                                                                           
#    parser.add_argument("-StudyDescription","--StudyDescription",action="store_true",help="Get StudyDescription")                                                      
#    parser.add_argument("-StudyID","--StudyID",action="store_true",help="Get StudyID")                                                                                 
#    parser.add_argument("-StudyInstanceUID","--StudyInstanceUID",action="store_true",help="Get StudyInstanceUID")                                                      
#    parser.add_argument("-StudyTime","--StudyTime",action="store_true",help="Get StudyTime")                                                                           
#    parser.add_argument("-TransmitCoilName","--TransmitCoilName",action="store_true",help="Get TransmitCoilName")                                                      
#    parser.add_argument("-VariableFlipAngleFlag","--VariableFlipAngleFlag",action="store_true",help="Get VariableFlipAngleFlag")                                       
#    parser.add_argument("-WindowCenter","--WindowCenter",action="store_true",help="Get WindowCenter")                                                                  
#    parser.add_argument("-WindowCenterWidthExplanation","--WindowCenterWidthExplanation",action="store_true",help="Get WindowCenterWidthExplanation")
