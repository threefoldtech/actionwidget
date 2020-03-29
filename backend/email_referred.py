import config


email_referral_subject = "Someone invited you to join the 3bot referral program"
email_referral = """
<b> Welcome to the 3bot referral program </b>

Use this link to join the referral program:

{LINK}

"""


def get_email_referred_text(userId):
    
    return email_referral.format(LINK = "{}/signup_referred?userid={}".format(config.URL, userId))

def get_email_referred_subject():
    return email_referral_subject
