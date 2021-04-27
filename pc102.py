import dropbox

import cv2
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        img_name = "img" + str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
take_snapshot()
print("image taken")

    def upload_file(img_name):
        """upload a file to Dropbox using API v2
        """
        access_token = 'HLT20_6a70sAAAAAAAAAARxw0r6tqcCTLV2RllLQvJQf29WfP2VFHUQniYsg7RX4'
        file=img_name
        file_from=file
        file_to='/Hasit/'+(img_name)
        dbx = dropbox.Dropbox(self.access_token)
    def main():
        access_token = 'HLT20_6a70sAAAAAAAAAARxw0r6tqcCTLV2RllLQvJQf29WfP2VFHUQniYsg7RX4'
        transferData = TransferData(access_token)

        file_from = input('enter the file you want to transfer to dropbox:-')
        file_to = input('enter the full path to upload to dropbox:-')  # The full path to upload the file to, including the file name

    # API v2
        transferData.upload_file(file_from, file_to)

        print('file has been moved')
main() 