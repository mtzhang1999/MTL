import cv2
import numpy as np

total = 0
total_ang_acc = 0

def ang_acc(vec_1, vec_2):
    # print(vec_1.shape, np.linalg.norm(vec_1, axis=2, keepdims=True).shape)
    vec_1 = vec_1/np.linalg.norm(vec_1, axis=2, keepdims=True)
    vec_2 = vec_2/np.linalg.norm(vec_2, axis=2, keepdims=True)
    return np.mean(np.sum(vec_1*vec_2, 2))
for i in range(7):
    name = "testset\\"+ '%03d' %i +"_normal.npy"
    normal = np.load(name)
    normal_rgb = np.zeros((480, 640, 3))
    normal_rgb[:,:,0] = normal[:,:,2]
    normal_rgb[:,:,1] = normal[:,:,1]
    normal_rgb[:,:,2] = normal[:,:,0]
    gt = cv2.imread("label\\normal_"+ '%03d' %(100+8*i) +".png")/255.

    cur_cos = ang_acc(normal_rgb, gt)

    total+=np.mean(np.abs(normal_rgb-gt))
    total_ang_acc+=cur_cos
print(total/7)
print(total_ang_acc/7)
