# 06 Sending Text Messages

from twilio.rest import Client # This class represents a client to twilio Rest API
import config

account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

client = Client(account_sid, auth_token)


client.messages.create(
    to = "...",
    from_ = "...", 
    body = """

this is our first message
"""
    )