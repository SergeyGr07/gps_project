def reading_file():
    st = [x.split(' ') for x in open('D:/coding/gps_project/data.txt').readlines()]
    datas = [x for x in st]
    message1 = " ".join(datas[14])
    message2 = " ".join(datas[15])
    message3 = " ".join(datas[16])
    messages = message1 + message2 + message3
    return messages


messages = reading_file()
