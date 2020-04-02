import config


email_reserve_name_subject = "Reserve your 3bot name"
email_reserve_name = """
Please instal the app to install the 3bot connect app and reserve your name


APPLINK APPSTORE + PLAYSTORE

"""




def get_email_reserve_name_text():
    return email_reserve_name #.format(LINK = "{}/status?verify_token={}".format(config.URL, verify_token))

def get_email_reserve_name_subject():
    return email_reserve_name_subject
