import numpy as np
import cv2

final_acc=0
final_iou=0
for i in range(0,7):

    seg = np.argmax(np.load("testset"+'%03d' %i+"_seg.npy"), axis=2)
    gt_seg = cv2.imread("label\13class_"+'%03d' %(550+i*8) +".png")[:,:,0]
  
    total_acc = 0
    total_iou = 0

    for i in range(13):
        mask1 = np.where(seg==i, 1, 0)
        mask2 = np.where(gt_seg==i, 1, 0)
        
        intersection = np.where(mask1+mask2==2, 1, 0)
        uni = np.where(mask1+mask2>0, 1, 0)

        uni_num = np.sum(uni)
        intersection_num = np.sum(intersection)

        if uni_num==0:
            iou=1
            acc=1
            total_acc+=acc
            total_iou+=iou
            continue
        elif np.sum(mask2)==0:
            acc=1
            iou=0
            total_acc+=acc                                                      
            total_iou+=iou
            continue
              
        acc = intersection_num/np.sum(mask2)
        iou = intersection_num/uni_num

        total_acc+=acc
        total_iou+=iou

    # print(total_acc/13)
    # print(total_iou/13)
    final_acc+=(total_acc/13)
    final_iou+=(total_iou/13)

print(final_acc/7)
print(final_iou/7)
