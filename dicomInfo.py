#!/ccnc_bin/venv/bin/python2.7
__author__='Kevin, Takwan and BeumJun'
__copyright__='CCNC'

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
    Input : dicom directory location
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


if __name__=='__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
            description = textwrap.dedent('''\
                    {codeName} : Returns information extracted from dicom within the directory
                    ====================
                        eg) {codeName}
                        eg) {codeName} -dir /Users/kevin/NOR04_CKI -o PatientID PatientName

                    Options: 
                    {infoList}
                    '''.format(codeName=os.path.basename(__file__),
                        infoList=', '.join(infoList))))

    parser.add_argument("-dir","--directory",help="Data directory location, default = pwd",default=os.getcwd())
    parser.add_argument("-dic","--dicom",help="Dicom location")
    parser.add_argument("-o","--option",nargs='+',help="Information to print. Choose from the options above")

    args = parser.parse_args()

    main(args)
