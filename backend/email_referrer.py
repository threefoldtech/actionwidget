import config


email_referral_subject = "Welcome to the 3bot referral program"
email_referral = """
<b> Welcome to the 3bot referral program </b>

Use this link to invite 10 people to join you:

{LINK}

"""


def get_email_referrer_text(verify_token):
    return email_referral.format(LINK = "{}/status?verify_token={}".format(config.URL, verify_token))

def get_email_referrer_subject():
    return email_referral_subject
