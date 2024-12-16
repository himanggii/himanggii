import smtplib

def send_email_vulnerable():
    server = smtplib.SMTP("mail.example.com", 25)  # No encryption
    server.login("admin@example.com", "password123")  # Hardcoded credentials
    server.sendmail("admin@example.com", "user@example.com", "Hello!")
    server.quit()

if __name__ == "__main__":
    send_email_vulnerable()
