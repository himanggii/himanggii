from ftplib import FTP

def ftp_example():
    ftp = FTP("ftp.dlptest.com")  # Public FTP server for testing
    ftp.login("dlpuser", "password")  # Login credentials
    
    # List files in the current directory
    ftp.retrlines('LIST')
    
    # Download a file
    with open("downloaded_file.txt", "wb") as f:
        ftp.retrbinary("RETR sample.txt", f.write)

    ftp.quit()

if __name__ == "__main__":
    ftp_example()
