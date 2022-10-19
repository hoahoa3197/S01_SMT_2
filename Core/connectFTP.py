import ftplib
import os
import base64

def readInfoSever():
    # print("[INFO] Preparing data...!")
    totalData = []
    package_dir = os.path.dirname(os.path.abspath(__file__))
    txtFile = os.path.join(package_dir, '../DefaultData/dataUpdateCode.txt')
    # txtFile = r"C:\Users\V3041045\Desktop\hongha\FATP_FT087_v0.0.1\DefaultData\dataUpdateCode.txt"
    with open(txtFile, "r") as r:
        data = r.read()
        listData = data.split("\n")
        for i in range(len(listData)):
            str = listData[i]
            if str == "":
                continue
            strBytes = str.encode("utf-8")
            strEncode = base64.b64decode(strBytes)
            strEncode = strEncode.decode("utf-8")
            data = strEncode.rstrip("\n")
            data = data.split(":")
            totalData.append(data[1])
            # print(data[1], "__________")
    # print('done!')
    print(totalData, "---------------")
    # print("[INFO] Ready to run!")
    return totalData


def uploadFiletoFtp(ftp, linkFile, currentDir):
    if (ftp.pwd()[1:] != currentDir):
        try:
            ftp.cwd(currentDir)
        except Exception:
            # cdTree("/".join(currentDir.split("/")[:-1]))
            ftp.mkd(currentDir)
            ftp.cwd(currentDir)
    name = os.path.split(linkFile)[1]
    try:
        with open(linkFile, "rb") as file:
            # use FTP's STOR command to upload the file
            res = ftp.storbinary(f"STOR {name}", file)
            print(res)
            if not res.startswith('226'):
                print('Upload failed', name)
                return False
            else:
                return True
    except:
        print('error to upload file: ', name)
        return False

if __name__=="__main__":
    FTP_HOST = "10.228.14.27"
    FTP_USER = "ie_admin"
    FTP_PASS = "iead123456"
    linkFile = r"C:\Users\V3041045\Desktop\hongha\FATP_FT087_v0.0.1\Data\saveImage\2020_11\02 10_16_48_718939.png"
    dir = "2020_11"
    currentDir = "_SFCData/SaveImgTest/%s" % (dir)
    uploadFiletoFtp(linkFile, dir)
    # package_dir = os.path.dirname(os.path.abspath(__file__))
    # link = os.path.join(package_dir, '../DefaultData/dataUpdateCode.txt')
    # print(link)