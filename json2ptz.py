import json
import glob
import os 

delname = []
filenames = glob.glob('C:/local/test/'+"*.json")
face = ['ChinContour','LeftEye','LeftEyeBrow','LeftPupil','Mouth','Nose','RightEye','RightEyeBrow','RightPupil']
for i in filenames:
    with open(i) as f:
        content = json.load(f)
        Face = content['Face']
        for j in face:
            if not 'Landmarks' in Face[j]:
                delname.append(i)
                print(os.path.basename(i))
                break
print(len(delname))
for i in delname:
    os.remove(i)
