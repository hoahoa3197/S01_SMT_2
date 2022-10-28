from re import U
import cv2
from pylibdmtx.pylibdmtx import decode
import zxingcpp
cap = cv2.VideoCapture(0)
cap.set(3,2048)
cap.set(4,2048)
while True:
    _,img = cap.read()
    img_resize = cv2.resize(img,(500,500))
    gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    resultScanCode = zxingcpp.read_barcodes(gray)
    if resultScanCode != []:
        for result in resultScanCode:
            if str(result.format) == "BarcodeFormat.DataMatrix" or str(result.format) == "BarcodeFormat.QRCode":
                print(result.text)
    # dataMatrix = decode(img)
        
    # print(dataMatrix)
    cv2.imshow("Frame",img_resize)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
