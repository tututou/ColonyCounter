import cv2
import matplotlib as mpl
import numpy as np
import os
mpl.use('TkAgg')
from matplotlib import pyplot as plt

class preProcess(object):

    LAPOFGAUSS_BLUR_SIZE = 7

    def __init__(self, img_path, **kwargs):
        # load img
        self.original_img = cv2.imread(img_path)
        print(self.original_img.shape)
        print(self.original_img.dtype)
        self.step_img = self.original_img.copy()

        # get minRad & maxRad
        self.minRad = kwargs.get('minRad', None)
        self.maxRad = kwargs.get('maxRad', None)
        self.thresValue = kwargs.get('thresValue', None)

        # results
        self.colonycount = None

    def correct_brightness(self):
        '''
        Remove noise from image, enhance edges
        '''
        # make background mask
        self.make_convoluted_mask()
        inverted_mask = cv2.bitwise_not(self.conv_mask)
        print('inv_mask',inverted_mask)

        # split channels
        #channels = cv2.split(self.original_img)
        # split a costly operation (in terms of time). Numpy indexing is much more efficient.
        blue = self.step_img[:,:,0]
        green = self.step_img[:,:,1]
        red = self.step_img[:,:,2]
        channels = [blue, green, red]

        self.display_images( channels, ['blue', 'green', 'red'], 1, 3)
        for idx,channel in enumerate(channels):
            print(channel.dtype)
            channel = cv2.subtract(channel, inverted_mask)
            r = 196.0 / channel.shape[1]
            print('r: ', r)

            conv = cv2.resize( channel, dsize=(0,0), fx = r, fy = r, interpolation = cv2.INTER_AREA);
            print('conv shape', conv.shape)
            cv2.imshow('conv', conv)
            conv = cv2.medianBlur(conv, 11);
            print('conv shape', conv.shape)
            conv = cv2.resize( conv, dsize=(self.original_img.shape[1],self.original_img.shape[0]), interpolation=cv2.INTER_LINEAR);
            print('channel shape', channel.shape)
            print('conv shape', conv.shape)
            print('mask shape', self.conv_mask.shape)

            # Extract Foreground mask?
            #channel = 255*(conv/self.conv_mask) - channel;
            div = cv2.divide(conv, self.conv_mask)
            channel = cv2.subtract(channel, div)
            self.display_images( [channel, div], ['channel subtract: ',idx,'div'], 1, 2)

            # Normalise image
            cv2.normalize(src = channel, dst = channel, alpha = 0, beta = 255, norm_type = cv2.NORM_MINMAX, dtype = -1, mask = self.conv_mask);
            self.display_images( [channel], ['channel '+str(idx)], 1, 1)

            # Subtract positive Laplacian of Gaussian or (add negative ?)
            channel = self.subtract_Lap_of_gaussian(channel, preProcess.LAPOFGAUSS_BLUR_SIZE)

            # cv2.convertScaleAbs()?

        # merge all channels into grayscale img
        # NEED TO CHECK IF PASS BY OBJ or REFERENCE
        self.gray = cv2.cvtColor(cv2.merge(channels), cv2.COLOR_BGR2GRAY)
        self.step_img = (channels[0]+channels[1]+channels[2])/3.0;
        self.display_images( [self.gray, self.step_img], ['gray','step_img'], 1, 2)

    def make_convoluted_mask(self):
        ''' All "mask" black image of size original(rows,col) '''
        self.conv_mask = np.full( (self.original_img.shape[0], self.original_img.shape[1]), 255, dtype = "uint8")

    def display_images(self, images, titles, rows, cols):
        for i in range(len(images)):
            plt.subplot(rows,cols,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
        plt.show()

    def subtract_Lap_of_gaussian(self, img_in, blur_size):
        '''
        https://github.com/qgeissmann/OpenCFU/blob/master/src/processor/src/Step_2.cpp#L26
        (Edge Detection)
        '''
        print('subtract lap of Gaussian ...')
        temp_mat = cv2.GaussianBlur(img_in, (blur_size, blur_size), 3)
        print('temp_mat gaus', temp_mat)
        cv2.imshow('temp_mat gaus', temp_mat)
        temp_mat = cv2.Laplacian(temp_mat, ddepth=cv2.CV_8U, ksize=5, scale=0.3)
        print('temp_mat lap', temp_mat)
        cv2.imshow('temp_mat lap', temp_mat)
        ret, temp = cv2.threshold(temp_mat, 10, 255, cv2.THRESH_BINARY)
        print('temp thres',temp)
        cv2.imshow('temp thres', temp)
        contoursToDraw = []

        #find contours
        _, contours, hierarchy = cv2.findContours(temp, mode=cv2.RETR_CCOMP, method=cv2.CHAIN_APPROX_SIMPLE)
        if len(contours) > 0:
            hierarchy = hierarchy[0]
            print('Total contours:', len(contours))
        # for k in range(len(contours)):
        #     # if the contour has no holes and if it is not a hole
        #     if hierarchy[k][2] < 0 and hierarchy[k][3] < 0:
        #         # std::copy(contours.begin()+k, contours.begin()+k+1, contoursToDraw.begin())
        #         #rect = cv2.boundingRect(contoursToDraw[0])
        #         rect = cv2.boundingRect(contours[k])
        #         # cv::drawContours(tmp_mat,contoursToDraw,0,cv::Scalar(0),-1,8, 1,cv::Point(-rect.x,-rect.y));
        #         cv2.drawContours(temp,contours[k],external_color=0, hole_color=-1, linetype = 8, max_level = 1, offset=(-rect.x,-rect.y))
            for k in zip(contours, hierarchy):
                cur_contour, cur_hierarchy = k[0], k[1]
                if cur_hierarchy[2] < 0: #and cur_hierarchy[3] < 0:
                    print(cur_contour)
                    approx = cv2.approxPolyDP(cur_contour,0.01*cv2.arcLength(cur_contour,True),True)
                    area = cv2.contourArea(cur_contour)
                    if ((len(approx) > 8) & (area > 30) ):
                        print('Area:{}, Approx: {}'.format(area, approx))
                        #x,y,w,h = cv2.boundingRect(cur_contour)
                        # rect = cv2.boundingRect(cur_contour)
                        contoursToDraw.append(cur_contour)
                        #cv2.rectangle(temp_mat,(x,y),(x+w,y+h),(0,0,255),3)
                        # cv2.drawContours(img, contours, k, (0, 255, 0), 2)

            if len(contoursToDraw) > 0:
                # draw contours onto image
                print('num contours:', len(contoursToDraw))
                self.colonycount = len(contoursToDraw)
                cv2.drawContours(temp_mat, contoursToDraw, -1, (255,0,0), 1)
                cv2.drawContours(self.original_img, contoursToDraw, -1, (255,0,0), 1)
        cv2.imshow('draw on temp_mat',temp_mat)
        out_img = cv2.subtract(img_in, temp)
        cv2.imshow('out_img', out_img)
        return out_img

if __name__ == '__main__':
    img = 'test_images/43.jpg'
    img_path = os.path.abspath(img)
    print(img_path)
    cc = preProcess(img_path)
    cc.correct_brightness()
    cc.display_images([cc.original_img, cc.gray], ['original','gray'], 1, 2)
    print(cc.colonycount)
