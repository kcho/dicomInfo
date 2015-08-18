#!/ccnc_bin/venv/bin/python2.7
__authors__=['Kevin','Takwan','BeumJun']

import textwrap
import dicom
import re
import os
import sys
import argparse

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

        #Looping through the bunch of files
        for singleFile in files:

            #if there is dicom files
            if re.search('.*ima|.*dcm|\d{8}',singleFile,flags=re.IGNORECASE):
                try:
                    firstDicomFile = dicom.read_file(os.path.join(root,singleFile))
                except:
                    firstDicomFile = dicom.read_file(os.path.join(root,singleFile),force=True)

                #make a switch to turn off the later loops
                switch='break'

                #turn the file loop off
                break
            else:
                switch='non-break'

        #if switch is on, turn the dir loop off
        if switch=='break':
            break
    return firstDicomFile


def getDicomInfo2(dicomFile):
    try:
        firstDicomFile = dicom.read_file(dicomFile)
    except:
        firstDicomFile = dicom.read_file(dicomFile,force=True)

    return firstDicomFile

def main(args):
    try:
        firstDicomFile = getDicomInfo(args.directory)
    except:
        firstDicomFile = getDicomInfo2(args.dicom)
   
   # if response == 'AccessionNumber':
   #     print firstDicomFile.AccessionNumber
   # if response == 'AcquisitionDate':
   #     print firstDicomFile.AcquisitionDate
   # if response == 'PatientName':
   #     print firstDicomFile.PatientName


    if args.AccessionNumber:
        print firstDicomFile.AccessionNumber
    if args.PatientName:
        print 'Patient Name:',firstDicomFile.PatientName
    if args.AcquisitionDate:
        print 'Acquisition Date:',firstDicomFile.AcquisitionDate
    if args.AcquisitionMatrix:
        print 'Acquisition Matrix:',firstDicomFile.AcquisitionMatrix
    if args.AcquisitionNumber:
        print 'Acquisition Number:',firstDicomFile.AcquisitionNumber
    if args.AcquisitionTime:
        print 'Acquisition Time:',firstDicomFile.AquisitionTime
    if args.AngioFlag:
        print 'Angio Flag:',firstDicomFile.AngioFlag
    if args.BitsAllocated:
        print 'Bits Allocated:',firstDicomFile.BitsAllocated
    if args.BitsStored:
        print 'Bits Stored:',firstDicomFile.BitsStored
    if args.Columns:
        print 'Columns:',firstDicomFile.Columns
    if args.ContentDate:
        print 'Content Date:',firstDicomFile.ContentDate
    if args.ContentTime:
        print 'Content Time:',firstDicomFile.ContentTime
    if args.DeviceSerialNumber:
        print 'Device Serial Number:',firstDicomFile.DeviceSerialNumber
    if args.EchoNumbers:
        print 'Echo Numbers:',firstDicomFile.EchoNumbers
    if args.EchoTime:
        print 'Echo Time:',firstDicomFile.EchoTime
    if args.EchoTrainLength:
        print 'Echo Train Length:',firstDicomFile.EchoTrainLength
    if args.FlipAngle:
        print 'Flip Angle:',firstDicomFile.FlipAngle
    if args.FrameOfReferenceUID:
        print 'Frame of Reference UID:',firstDicomFile.FrameOfReferenceUID
    if args.HighBit:
        print 'High Bit:',firstDicomFile.HighBit
    if args.ImageOrientationPatient:
        print 'Image Oreigntation Patient:',firstDicomFile.ImageOrientationPatient
    if args.ImagePositionPatient:
        print 'Image Position Patient:',firstDicomFile.ImagePositionPatient
    if args.ImageType:
        print 'Image Type:',firstDicomFile.ImageType
    if args.ImagedNucleus:
        print 'Imaged Nucleus:',firstDicomFile.ImagedNucleus
    if args.ImagingFrequency:
        print 'Imaging Frequency:',firstDicomFile.ImagingFrequency
    if args.InPlanePhaseEncodingDirection:
        print 'In Plane Phase Encoding Direction:',firstDicomFile.InPlanePhaseEncodingDirection
    if args.InstanceCreationDate:
        print 'Instance Creation Date:',firstDicomFile.InstanceCreationDate
    if args.InstanceNumber:
        print 'Instance Number:',firstDicomFile.InstanceNumber
    if args.InstitutionAddress:
        print 'Institution Address:',firstDicomFile.InstitutionAddress
    if args.InstitutionName:
        print 'Institution Name:',firstDicomFile.InstitutionName
    if args.InstitutionalDepartmentName:
        print 'Institutional Department Name:',firstDicomFile.InstitutionalDepartmentName
    if args.LargestImagePixelValue:
        print 'Largest Image Pixel Value:',firstDicomFile.LargestImagePixelValue
    if args.MRAcquisitionType:
        print 'MR Acquisition Type:',firstDicomFile.MRAcquisitionType
    if args.MagneticFieldStrength: 
        print 'Magnetic Field Strength:',firstDicomFile.MagneticFieldStrength
    if args.Manufacturer:
        print 'Manufacturer:',firstDicomFile.Manufacturer
    if args.ManufacturerModelName:
        print 'Manufacturer Model Name:',firstDicomFile.ManufacturerModelName
    if args.Modality:
        print 'Modality:',firstDicomFile.Modality
    if args.NumberOfAverages:
        print 'Number of Averages:',firstDicomFile.NumberOfAverages
    if args.NumberOfPhaseEncodingSteps:
        print 'Number of Phase Encoding Steps:',firstDicomFile.NumberOfPhaseEncodingSteps
    if args.OperatorsName:
        print 'Operators Name:',firstDicomFile.OperatorsName
    if args.PatientAge:
        print 'Patient Age:',firstDicomFile.PatientAge
    if args.PatientBirthDate:
        print 'Patient Birth Date:',firstDicomFile.PatientBirthDate
    if args.PatientID:
        print 'Patient ID:',firstDicomFile.PatientID
    if args.PatientPosition:
        print 'Patient Position:',firstDicomFile.PatientPosition
    if args.PatientSex:
        print 'Patient Sex:',firstDicomFile.PatientSex
    if args.PatientWeight:
        print 'Patient Weight:',firstDicomFile.PatientWeight
    if args.PercentPhaseFieldOfView:
        print 'Percent Phase Field Of View:',firstDicomFile.PercentPhaseFieldOfView
    if args.PercentSampling:
        print 'Percent Sampling:',firstDicomFile.PercentSampling
    if args.PerformedProcedureStepDescription:
        print 'Performed Procedure Step Description:',firstDicomFile.PerformedProcedureStepDescription
    if args.PerformedProcedureStepID:
        print 'Performed Procedure Step ID:',firstDicomFile.PerformedProcedureStepID
    if args.PerformedProcedureStepStartDate:
        print 'Performed Procedure Step Start Date:',firstDicomFile.PerformedProcedureStepStartDate
    if args.PerformedProcedureStepStartTime:
        print 'Performed Procedure Step Start Time:',firstDicomFile.PerformedProcedureStepStartTime
    if args.PerformingPhysicianName:
        print 'Performing Physician Name:',firstDicomFile.PerformingPhysicianName
    if args.PhotometricInterpretation:
        print 'Photometric Interpretation:',firstDicomFile.PhotometricInterpretation
    if args.PhysiciansOfRecord:
        print 'Physicians Of Record:',firstDicomFile.PhysiciansOfRecord
    if args.PixelBandwidth:
        print 'Pixel Bandwidth:',firstDicomFile.PixelBandwidth
    if args.PixelData:
        print 'Pixel Data:',firstDicomFile.PixelData
    if args.PixelRepresentation:
        print 'Pixel Representation:',firstDicomFile.PixelRepresentation
    if args.PixelSpacing:
        print 'Pixel Spacing:',firstDicomFile.PixelSpacing
    if args.PositionReferenceIndicator:
        print 'Position Reference Indicator:',firstDicomFile.PositionReferenceIndicator
    if args.ProtocolName:
        print 'Protocol Name:',firstDicomFile.ProtocolName
    if args.RefdImageSequence:
        print 'Refd Image Sequence:',firstDicomFile.RefdImageSequence
    if args.ReferencedImageSequence:
        print 'Referenced Image Sequence:',firstDicomFile.ReferencedImageSequence
    if args.ReferringPhysicianName:
        print 'Referring Physician Name:',firstDicomFile.ReferringPhysicianName
    if args.RepetitionTime:
        print 'Repetition Time:',firstDicomFile.RepetitionTime
    if args.RequestAttributesSequence:
        print 'Request Attributes Sequence:',firstDicomFile.RequestsAttributeSequence
    if args.RequestedProcedureDescription:
        print 'Requested Procedure Description:',firstDicomFile.RequestedProcedureDescription
    if args.RequestingPhysician:
        print 'Requesting Physician:',firstDicomFile.RequestingPhysician
    if args.Rows:
        print 'Rows:',firstDicomFile.Rows
    if args.SAR:
        print 'SAR:',firstDicomFile.SAR
    if args.SOPClassUID:
        print 'SOP Class UID:',firstDicomFile.SOPClassUID
    if args.SOPInstanceUID:
        print 'SOP Instance UID:',firstDicomFile.SOPInstanceUID
    if args.SamplesPerPixel:
        print 'Samples Per Pixel:',firstDicomFile.SamplesPerPixel
    if args.ScanOptions:
        print 'Scan Options:',firstDicomFile.ScanOptions
    if args.ScanningSequence:
        print 'Scanning Sequence:',firstDicomFile.ScanningSequence
    if args.SequenceName:
        print 'Sequence Name:',firstDicomFile.SequenceName
    if args.SequenceVariant:
        print 'Sequence Variant:',firstDicomFile.SequenceVariant
    if args.SeriesDate:
        print 'Series Date:',firstDicomFile.SeriesDate
    if args.SeriesDescription:
        print 'Series Description:',firstDicomFile.SeriesDescription
    if args.SeriesInstanceUID:
        print 'Series Instance UID:',firstDicomFile.SeriesInstanceUID
    if args.SeriesNumber:
        print 'Series Number:',firstDicomFile.SeriesNumber
    if args.SeriesTime:
        print 'Series Time:',firstDicomFile.SeriesTime
    if args.SliceLocation:
        print 'Slice Location:',firstDicomFile.SliceLocation
    if args.SliceThickness:
        print 'Slice Thickness:',firstDicomFile.SliceThickness
    if args.SmallestImagePixelValue:
        print 'Smallest Image Pixel Value:',firstDicomFile.SmallestImagePixelValue
    if args.SoftwareVersions:
        print 'Software Versions:',firstDicomFile.SoftwareVersions
    if args.SpacingBetweenSlices:
        print 'Spacing Between Slices:',firstDicomFile.SpacingBetweenSlices
    if args.StationName:
        print 'Station Name:',firstDicomFile.StationName
    if args.StudyDate:
        print 'Study Date:',firstDicomFile.StudyDate
    if args.StudyDescription:
        print 'Study Description:',firstDicomFile.StudyDescription
    if args.StudyID:
        print 'Study ID:',firstDicomFile.StudyID
    if args.StudyInstanceUID:
        print 'Study Instance UID:',firstDicomFile.StudyInstanceUID
    if args.StudyTime:
        print 'Study Time:',firstDicomFile.StudparseryTime
    if args.TransmitCoilName:
        print 'Transmit Coil Name:',firstDicomFile.TransmitCoilName
    if args.VariableFlipAngleFlag:
        print 'Variable Flip Angle Flag:',firstDicomFile.VariableFlipAngleFlag
    if args.WindowCenter:
        print 'Window Center:',firstDicomFile.WindowCenter
    if args.WindowCenterWidthExplanation:
        print 'Window Center Width Explanation:',firstDicomFile.WindowCenterWidthExplanation


    


           #parser.add_argument('-t','--tak',action='store_true',help="Print tak's information")

  #  except:
        #print re.findall('\x08\x00(\d{8})\x10\x00',' '.join(firstDicomFile.MediaStorageSOPClassUID[5])),
        #print re.findall('\x08\x00(\d{8})\x10\x00',' '.join(firstDicomFile.MediaStorageSOPClassUID[6]))

       # print firstDicomFile
  #      print 'Data Displayed'

        #four = re.findall('\x08\x00(\d{8})\x10\x00',firstDicomFile.MediaStorageSOPClassUID[4])
        #five = re.findall('\x08\x00(\d{8})\x10\x00',firstDicomFile.MediaStorageSOPClassUID[5])
        #six = re.findall('\x08\x00(\d{8})\x10\x00',firstDicomFile.MediaStorageSOPClassUID[6])

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
