import dropbox
import os
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from):
            for fileName in files:
                local_path=os.path.join(root,fileName)
                relative_path=os.path.relpath(local_path,file_from)
                dropbox_path=os.path.join(file_to,relative_path)
                with open(local_path,'rb') as f:
                    dbx.files_upload(f.read(),dropbox_path,mode=WriteMode('overwrite'))

        
def main():
    access_token='sl.BH7p1NcfgLIhNiHPocIPBvTWal0FcEvC0L0d_6PdQws3MhrQ0jfhZRFXN5YjgFB523F3levU7MuLkAm9DxkY_ivwWXZJ0hqR3lgoUdHUI32AWmrDlaXyWFEvcCRlWDAuk27K1VqkFF0'
    transferdata=TransferData(access_token)    
    file_from=input("enter the file to transfered: ")
    file_to=input("enter the dropbox path: ")
    transferdata.upload_file(file_from,file_to)
    print("file has been moved")
main()        
