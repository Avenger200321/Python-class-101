import dropbox
class Automatic:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dxb=dropbox.Dropbox(self.access_token)
        with open(file_from, 'rb') as f:
            dxb.files_upload(f.read(),file_to)

def main():
    access_token='sl.Av7KViPvq1G2IJ4GFKxDmhn63AKo5fHSSH1hEbql466pdE31NTiArSnTeJBKdAvTumXI6razvcyRDsjC1k1UJ0nhIO7YJNMG4loFj_s-pbpQDdKYY82qG4XackebIMb4E9eLqVI'
    autom = Automatic(access_token)
    file_from = 'Test.txt'
    file_to = '/Python Class 101/test.txt'
    autom.upload_file(file_from, file_to)
if __name__ == '__main__':
    main()