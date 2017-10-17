#include <opencv2/core/core.hpp> 
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <stdio.h>
#include <iostream>

using namespace cv;
using namespace std;


int main() 
{
    Mat img = imread("imagen.jpg", CV_LOAD_IMAGE_UNCHANGED); 
   
    if (!img.data ) 
    {
        cout << "No se pudo abrir la imagen.\n";
        return -1; 
    }
    /* for(int i = 0; i < img.rows; i++)
    {
        for(int j = 0; j < img.cols; j++)
        {
            Vec3b bgrPixel0 = img.at<Vec3b>(i, j);
            Vec3b bgrPixel1 = img.at<Vec3b>(i-1, j);
            Vec3b bgrPixel2 = img.at<Vec3b>(i, j+1);
            Vec3b bgrPixel3 = img.at<Vec3b>(i+1, j);
            Vec3b bgrPixel4 = img.at<Vec3b>(i, j-1);
            bgrPixel0.val[0] = ((int)bgrPixel0.val[0]+int(bgrPixel1.val[0])+int(bgrPixel2.val[0])+int(bgrPixel3.val[0])+int(bgrPixel4.val[0]))/5; // B
            bgrPixel0.val[1] = (int(bgrPixel0.val[1])+int(bgrPixel1.val[1])+int(bgrPixel2.val[1])+int(bgrPixel3.val[1])+int(bgrPixel4.val[1]))/5; // G
            bgrPixel0.val[2] = (int(bgrPixel0.val[2])+int(bgrPixel1.val[2])+int(bgrPixel2.val[2])+int(bgrPixel3.val[2])+int(bgrPixel4.val[2]))/5; // R
        }
    } */
    
    blur(img,img,Size(10,10)); 
    
    
    namedWindow( "bat", CV_WINDOW_AUTOSIZE ); 

    imshow( "bat", img ); 

    waitKey(0);
    
    return 0;
}
 
