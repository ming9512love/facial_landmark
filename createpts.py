import json
import glob
import numpy as np

filenames = glob.glob('G:/大学院/代码练习/facial_landmark/test/'+"*.json")
face = ['ChinContour','LeftEye','LeftEyeBrow','LeftPupil','Mouth','Nose','RightEye','RightEyeBrow','RightPupil']
for i in filenames[:1]:
    with open(i) as f:
        content = json.load(f)
        Face = content['Face']
        landmark60 = []
        for j in face:
            landmark60 += Face[j]['Landmarks']
        landmark60 = np.array(landmark60)
    with open('G:/大学院/代码练习/facial_landmark/test.pts','w') as f2:
        for i in range(60):
            f2.write(''.join('%s' %id for id in landmark60[i]))

# print(landmark60)
# print(landmark60.shape)


# with open('test.pts') as f:
    