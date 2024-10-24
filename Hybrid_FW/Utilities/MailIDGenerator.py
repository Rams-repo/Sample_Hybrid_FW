from datetime import datetime


def get_new_mailid():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "ram" + time_stamp + "@gmail.com"
