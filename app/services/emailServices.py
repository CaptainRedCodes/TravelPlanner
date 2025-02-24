import aiosmtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

async def send_verification_email(user_email: str, verification_token: str):
    sender_email = "rahulv2915102002@gmail.com"
    
    # Generate email verification link
    #verification_link = f"https://yourdomain.com/verify/{verification_token}"  --prod

    verification_link = f"http://127.0.0.1:8000/auth/verify-email/{verification_token}"  
    print(f"Verification Link: {verification_link}")


    subject = "Verify Your Email to Activate Your Account"
    body = f"Click the link below to verify your email:\n\n{verification_link}\n\nThis link will expire in 24 hours."

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = user_email
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    # Send email using aiosmtplib with OAuth2 authentication
    await aiosmtplib.send(
        message,
        hostname="smtp.gmail.com",  # Adjust if using another SMTP provider
        port=465,
        use_tls=True,
        username=sender_email,
        password=os.getenv("EMAIL_APP_PASSWORD"),  # Use OAuth2 token or App Password
    )
