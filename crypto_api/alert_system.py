# Setting up email alerts as desired. Replace generic sender, receiver, etc. fields for customizing alerts.
import smtplib

def send_email_alert(price):
    threshold = 2500  # Example threshold. Adjust as necessary.

    if price > threshold:
        # Setup email parameters
        sender_email = "your_email@gmail.com"
        receiver_email = "receiver_email@gmail.com"
        password = "your_email_password"  # For demonstration purposes only.
        subject = "Crypto Price Alert"
        body = f"The average crypto price is now: ${price}"

        message = f"Subject: {subject}\n\n{body}"

        # Send the email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
