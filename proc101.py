import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb') 
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'HLT20_6a70sAAAAAAAAAARxw0r6tqcCTLV2RllLQvJQf29WfP2VFHUQniYsg7RX4'
    transferData = TransferData(access_token)

    file_from = input('enter the folder you want to transfer to dropbox:-')
    file_to = input('enter the full path to upload to dropbox:-')  

    
    transferData.upload_file(file_from, file_to)

    print('folder has been moved')
main()