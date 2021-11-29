import dropbox
class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    

    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        openf=open(file_from,"rb")
        dbx.files_upload(openf.read(),file_to)

def t():
    access_token="sl.A9OqseWTzx5u3Acs1iTmwPDqWsvNgPyhW2Oudvjf40JrUO7TUyBWUlWlfyEB5zm0DC3A5R1enyqas8S3Qnt_8qasuVcrah5AxoV2bP7U4qs6-xSLthBDoXXQkQRXd4KQDe8bnbV5UPkM"
    transferData=TransferData(access_token)
    file_from=input("enter the file you want to tranfer:\n")
    file_to=input("enter the file destination:\n")
    transferData.upload_file(file_from,file_to)
    print("file has bee succesfully transferred!")
t()        
