def check_question(message):
    list_question_signal=["nhỉ","ai","ở đâu","đi đâu","bao giờ","khi nào","lúc nào","hồi nào","vì sao","tại sao","làm sao","thế nào","gì","bao nhiêu","mấy","?"]
    for signal in list_question_signal:
        if signal in message.lower():
            return True
    if message.split(" ")[-1].lower()=="chưa":
        return True
    return False

