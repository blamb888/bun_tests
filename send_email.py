import yagmail

def send_email(recipient, subject, body):
    try:
        with yagmail.SMTP('blamb888@gmail.com') as yag:
            yag.send(
                to=recipient,
                subject=subject,
                contents=body
            )
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    recipient_email = input("Please enter the recipient's email address: ")
    email_subject = input("Please enter the email subject: ")
    message_body = input("Please enter your message: ")

    if send_email(recipient_email, email_subject, message_body):
        print("Email sent successfully!")
    else:
        print("Failed to send the email.")
