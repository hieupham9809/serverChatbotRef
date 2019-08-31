def check_question(message):
    list_question_signal=["thế","nhỉ"," ai ","ở đâu","đi đâu","bao giờ","khi nào","lúc nào","hồi nào","vì sao","tại sao","làm sao","thế nào","gì","bao nhiêu","mấy","?"]
    for signal in list_question_signal:
        if signal in message.lower():
            print(signal)
            return True
    if message.split(" ")[-1].lower()=="chưa" or message.split(" ")[-1].lower()=="vậy":
        return True
    return False

# check_question("hieupham989@gmail.com nha, số điện thoại là 0961508884")

