import cv2
import numpy as np
for k in range(50):
    print(k)
    seg = cv2.imread("D:\Replica_Dataset\\room_0\Sequence_1\semantic_class\\semantic_class_"+str(k * 10)+".png", cv2.IMREAD_UNCHANGED)
    new_seg = np.zeros((480,640))
    for i in range(480):
        for j in range(640):
            if seg[i][j] in [7]:
                new_seg[i][j]=0
            elif seg[i][j] in [13]:
                new_seg[i][j]=1
            elif seg[i][j] in [31]:
                new_seg[i][j]=2
            elif seg[i][j] in [20]:
                new_seg[i][j]=3
            elif seg[i][j] in [40]:
                new_seg[i][j]=4
            elif seg[i][j] in [59]:
                new_seg[i][j]=7
            elif seg[i][j] in [76]:
                new_seg[i][j]=8
            elif seg[i][j] in [80]:
                new_seg[i][j]=9
            elif seg[i][j] in [87]:
                new_seg[i][j]=10
            elif seg[i][j] in [93]:
                new_seg[i][j]=11
            elif seg[i][j] in [97]:
                new_seg[i][j]=12
            elif seg[i][j] in [47, 12, 29, 37, 61, 56, 43, 98, 63, 60, 18, 10, 66, 71, 11, 54, 50, 33, 6, 74, 2, 39, 46, 94, 30, 49, 70, 77, 88, 67, 78, 26, -1, 45, 73, 84, 34, 62, 8, 4, 32, 52]:
                new_seg[i][j]=5
            else:
                new_seg[i][j]=6
                
    cv2.imwrite("D:\Replica_Dataset\\room_0\\new_room_0_sampled\label\\"+"%03d" %k +".png", new_seg)