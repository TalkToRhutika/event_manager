import smtplib
from builtins import ValueError, dict, str
from settings.config import settings
from app.utils.smtp_connection import SMTPClient
from app.utils.template_manager import TemplateManager
from app.models.user_model import User
import logging

class EmailService:
    def __init__(self, template_manager: TemplateManager):
        """Initialize the EmailService with SMTP client and template manager."""
        try:
            self.smtp_client = SMTPClient(
                server=settings.smtp_server,
                port=settings.smtp_port,
                username=settings.smtp_username,
                password=settings.smtp_password
            )
            self.template_manager = template_manager
        except Exception as e:
            logging.error(f"Error initializing SMTPClient: {e}")
            raise ValueError("Failed to initialize email service.")

    async def send_user_email(self, user_data: dict, email_type: str):
        """Send an email based on the user data and email type."""
        subject_map = {
            'email_verification': "Verify Your Account",
            'password_reset': "Password Reset Instructions",
            'account_locked': "Account Locked Notification"
        }

        if email_type not in subject_map:
            logging.error(f"Invalid email type: {email_type}")
            raise ValueError("Invalid email type provided.")

        # Render email content from template
        try:
            html_content = self.template_manager.render_template(email_type, **user_data)
        except Exception as e:
            logging.error(f"Error rendering template for {email_type}: {e}")
            raise ValueError(f"Error rendering the email template for {email_type}")

        # Send the email via SMTP client
        try:
            self.smtp_client.send_email(subject_map[email_type], html_content, user_data['email'])
            logging.info(f"Email sent successfully to {user_data['email']} for {email_type}")
        except smtplib.SMTPException as e:
            logging.error(f"SMTP error while sending email to {user_data['email']}: {e}")
            raise ConnectionError(f"Failed to send the email due to SMTP error: {e}")
        except Exception as e:
            logging.error(f"Unexpected error while sending email to {user_data['email']}: {e}")
            raise

    async def send_verification_email(self, user: User):
        """Send an email verification link to the user."""
        try:
            verification_url = f"{settings.server_base_url}verify-email/{user.id}/{user.verification_token}"
            await self.send_user_email({
                "name": user.first_name,
                "verification_url": verification_url,
                "email": user.email
            }, 'email_verification')
        except ValueError as ve:
            logging.error(f"Validation error while sending verification email to {user.email}: {ve}")
            raise
        except ConnectionError as ce:
            logging.error(f"Connection error while sending verification email to {user.email}: {ce}")
            raise
        except Exception as e:
            logging.error(f"Unexpected error while sending verification email to {user.email}: {e}")
            raise