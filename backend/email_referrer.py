import config


email_referral_subject = "Welcome to the 3bot referral program"
email_referral = """
<b> Welcome to the 3bot referral program </b>

Use this link to invite 10 people to join you:

{LINK}

"""


def get_email_referrer_text(secret):
    return email_referral.format(LINK = "{}/referral?secret={}".format(config.URL, secret))

def get_email_referrer_subject():
    return email_referral_subject
