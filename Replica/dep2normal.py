import cv2
import numpy as np
import os

for i in range(50):
    d_im = cv2.imread('D:\Replica_Dataset\\office_2\Sequence_2\\depth\\depth_' + str(300 + i * 10) + '.png', cv2.IMREAD_UNCHANGED).astype(float)
    print(d_im.shape)
    #cv2.imwrite("depth.jpg", d_im)
        # print(d_im.shape)
        # print(d_im)
    zy, zx = np.gradient(d_im)

    zy = zy*1
    zx = zx*1

    np.set_printoptions(threshold=np.inf)
    #print(d_im[380:460, 0:50], zx[380:460, 0:50], zy[380:460, 0:50])

    normal = np.dstack((-zx, -zy, np.ones_like(d_im)))
    n = np.linalg.norm(normal, axis=2)
    normal[:, :, 0] /= n
    normal[:, :, 1] /= n
    normal[:, :, 2] /= n

        # offset and rescale values to be in 0-255
    normal += 1
    normal /= 2
    normal *= 255
        # print(normal.shape)
        # normal = cv2.cvtColor(normal[:, :, ::-1], cv2.COLOR_RGB2BGR)

    cv2.imwrite('D:\Replica_Dataset\\office_2\\new_office_2_sampled\\normal\\' + "%03d" %i + ".png", normal[:, :, :])
#nor = cv2.imread(os.path.join(normaldir,d))
#cv2.imwrite("nor.jpg", nor)