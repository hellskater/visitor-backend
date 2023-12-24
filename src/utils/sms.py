from telesign.messaging import MessagingClient  # type: ignore

from settings import SETTINGS


def send_sms(phone_number: str, message: str, message_type: str = "ARN") -> None:
    if not all(
        [
            SETTINGS.TELESIGN_CUSTOMER_ID,
            SETTINGS.TELESIGN_API_KEY,
            phone_number,
            message,
        ]
    ):
        raise ValueError("Missing required parameters for sending SMS")

    messaging = MessagingClient(
        SETTINGS.TELESIGN_CUSTOMER_ID, SETTINGS.TELESIGN_API_KEY
    )
    response = messaging.message(phone_number, message, message_type)

    # For debugging purposes, print the response body
    print(f"\nResponse:\n{response.body}\n")
