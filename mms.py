from etext import *
from etext.providers import PROVIDERS
import os

try:
    text_email = os.environ["text_email"]
    text_password = os.environ["text_password"]
    sender_credentials = (text_email, text_password)
    mime_maintype = "image"
    mime_subtype = "png"
except KeyError as k:
    print(f"The variable {k} is missing.")


def send_mms(phone_number, message, file_path, subject, provider):
    if provider == "Other":
        for provider in PROVIDERS.keys():
            if PROVIDERS[provider]["mms_support"]:
                send_mms_via_email(
                    phone_number,
                    message,
                    file_path,
                    mime_maintype,
                    mime_subtype,
                    provider,
                    sender_credentials,
                    subject
                )
    elif PROVIDERS[provider]["mms_support"]:
        send_mms_via_email(
            phone_number,
            message,
            file_path,
            mime_maintype,
            mime_subtype,
            provider,
            sender_credentials,
            subject
        )
