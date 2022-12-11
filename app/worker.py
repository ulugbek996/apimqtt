import datetime

value = "17,9"

def vaqt_uzgartirish(vaqt):
    vaqt = vaqt.split("+")[0]
    vaqt = datetime.datetime.strptime(vaqt, "%y/%m/%d,%H:%M:%S")
    vaqt = vaqt + datetime.timedelta(hours=5)
    return vaqt.strftime("%y/%m/%d,%H:%M:%S")


def change_str_float(value):
    value = value.replace(",", ".")
    return float(value)


def change_str_tuple(stringtuple):
    stringtuple = stringtuple.split(",")
    return tuple(stringtuple)