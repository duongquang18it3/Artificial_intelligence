import cv2
import numpy as np
import matplotlib.pyplot as plt

trainData = np.random.randint(0, 100, (25, 2)).astype(np.float32);
ketqua = np.random.randint(0, 2, (25, 1)).astype(np.float32);

#Tạo một điểm có tọa độ
red = trainData[ketqua.ravel()==1]
blue = trainData[ketqua.ravel()==0]
newMember = np.random.randint(0, 100, (1, 2)).astype(np.float32);

plt.scatter(red[:,0],red[:,1], 100, 'r','s')
plt.scatter(blue[:,0],blue[:,1], 100, 'b','^')
plt.scatter(newMember[:,0],newMember[:,1], 100, 'g','o')

#Hàm KNearest_create() khỏi tạo thuật toán
#khởi tạo biến knn
knn = cv2.ml.KNearest_create()

#train dữ liệu từ trainData
knn.train(trainData, 0, ketqua)

temp, ketqua, hangxom, khoangcach = knn.findNearest(newMember, 5)

print("ketqua: {}\n".format(ketqua));
print("gannhat: {}\n".format(hangxom));
print("khoang cach: {}\n".format(khoangcach));
plt.show()
