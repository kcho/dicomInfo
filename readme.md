#dicomInfo.py

**It prints dicom information**

Either a target directory or a dicom file location could be given as an input.


*Dependency : nibabel (http://nipy.org/nibabel/)*

---


** Example **

    dicomInfo.py -h

    dicomInfo.py -o PatientName EchoTime

    dicomInfo.py -dir /Users/user/T1dicoms -o RepetitionTime

    dicomInfo.py -dic /Users/user/T1dicoms/1.dcm -o RepetitionTime

