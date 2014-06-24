#!/Users/admin/anaconda/bin/python

import textwrap
import dicom
import re
import os
import sys
import argparse


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
            if re.search('.*ima|.*dcm',singleFile,flags=re.IGNORECASE):

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


def main(args):

    firstDicomFile = getDicomInfo(args.directory)

    try:
        if args.all:
            print firstDicomFile
        if args.name:
            print firstDicomFile.PatientName
        if args.id:
            print firstDicomFile.PatientID
        if args.sex:
            print firstDicomFile.PatientSex
        if args.dob:
            print firstDicomFile.PatientBirthDate
        if args.date:
            print firstDicomFile.StudyDate

    except:
        #print re.findall('\x08\x00(\d{8})\x10\x00',' '.join(firstDicomFile.MediaStorageSOPClassUID[5])),
        #print re.findall('\x08\x00(\d{8})\x10\x00',' '.join(firstDicomFile.MediaStorageSOPClassUID[6]))

        four = re.findall('\x08\x00(\d{8})\x10\x00',firstDicomFile.MediaStorageSOPClassUID[4])
        five = re.findall('\x08\x00(\d{8})\x10\x00',firstDicomFile.MediaStorageSOPClassUID[5])
        six = re.findall('\x08\x00(\d{8})\x10\x00',firstDicomFile.MediaStorageSOPClassUID[6])

        if four != []:
            print four
        elif five != []:
            print five
        else:
            print six



if __name__=='__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description = textwrap.dedent('''\
                    {codeName} : Returns information extracted from dicom within the directory
                    ====================
                        eg) {codeName}
                        eg) {codeName} --dir /Users/kevin/NOR04_CKI
                    '''.format(codeName=os.path.basename(__file__))))

            #epilog="By Kevin, 26th May 2014")
    parser.add_argument('-dir','--directory',help='Data directory location, default = pwd',default=os.getcwd())
    parser.add_argument('-n','--name',action='store_true',help='Get patient name')
    parser.add_argument('-i','--id',action='store_true',help='Get patient ID')
    parser.add_argument('-s','--sex',action='store_true',help='Get patient sex')
    parser.add_argument('-b','--dob',action='store_true',help='Get patient DOB')
    parser.add_argument('-d','--date',action='store_true',help='Get scan date')
    parser.add_argument('-a','--all',action='store_true',help='Print all information')
    args = parser.parse_args()

    main(args)

# 'AccessionNumber', 'AcquisitionDate', 'AcquisitionMatrix', 'AcquisitionNumber', 'AcquisitionTime', 'AngioFlag', 'BitsAllocated', 'BitsStored', 'Columns', 'ContentDate', 'ContentTime', 'DeviceSerialNumber', 'EchoNumbers', 'EchoTime', 'EchoTrainLength', 'FlipAngle', 'FrameOfReferenceUID', 'HighBit', 'ImageOrientationPatient', 'ImagePositionPatient', 'ImageType', 'ImagedNucleus', 'ImagingFrequency', 'InPlanePhaseEncodingDirection', 'InstanceCreationDate', 'InstanceCreationTime', 'InstanceNumber', 'InstitutionAddress', 'InstitutionName', 'InstitutionalDepartmentName', 'LargestImagePixelValue', 'MRAcquisitionType', 'MagneticFieldStrength', 'Manufacturer', 'ManufacturerModelName', 'Modality', 'NumberOfAverages', 'NumberOfPhaseEncodingSteps', 'OperatorsName', 'PatientAge', 'PatientBirthDate', 'PatientID', 'PatientName', 'PatientPosition', 'PatientSex', 'PatientWeight', 'PercentPhaseFieldOfView', 'PercentSampling', 'PerformedProcedureStepDescription', 'PerformedProcedureStepID', 'PerformedProcedureStepStartDate', 'PerformedProcedureStepStartTime', 'PerformingPhysicianName', 'PhotometricInterpretation', 'PhysiciansOfRecord', 'PixelBandwidth', 'PixelData', 'PixelRepresentation', 'PixelSpacing', 'PositionReferenceIndicator', 'ProtocolName', 'RefdImageSequence', 'ReferencedImageSequence', 'ReferringPhysicianName', 'RepetitionTime', 'RequestAttributesSequence', 'RequestedProcedureDescription', 'RequestingPhysician', 'Rows', 'SAR', 'SOPClassUID', 'SOPInstanceUID', 'SamplesPerPixel', 'ScanOptions', 'ScanningSequence', 'SequenceName', 'SequenceVariant', 'SeriesDate', 'SeriesDescription', 'SeriesInstanceUID', 'SeriesNumber', 'SeriesTime', 'SliceLocation', 'SliceThickness', 'SmallestImagePixelValue', 'SoftwareVersions', 'SpacingBetweenSlices', 'StationName', 'StudyDate', 'StudyDescription', 'StudyID', 'StudyInstanceUID', 'StudyTime', 'TransmitCoilName', 'VariableFlipAngleFlag', 'WindowCenter', 'WindowCenterWidthExplanation', 'WindowWidth', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__eq__', '__format__', '__ge__', '__getattr__', '__getattribute__', '__getitem__', '__gt__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_character_set', '_get_pixel_array', '_pixel_data_numpy', '_pretty_str', 'add', 'add_new', 'clear', 'copy', 'dBdt', 'data_element', 'decode', 'dir', 'formatted_lines', 'fromkeys', 'get', 'group_dataset', 'has_key', 'items', 'iterall', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pixel_array', 'pop', 'popitem', 'remove_private_tags', 'save_as', 'setdefault', 'top', 'trait_names', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues', 'walk'
