from ftplib import FTP

def ftp_vulnerable():
    ftp = FTP("ftp.example.com")
    ftp.login("admin", "password123")  # Hardcoded credentials
    ftp.retrlines('LIST')
    ftp.quit()

if __name__ == "__main__":
    ftp_vulnerable()
