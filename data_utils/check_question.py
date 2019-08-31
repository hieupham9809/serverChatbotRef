def check_question(message):
    #bắt WH question 
    list_question_signal=["thế","nhỉ"," ai"," ai ","ở đâu","ở mô","đi đâu","bao giờ","bao lâu","khi nào","lúc nào","hồi nào","vì sao","tại sao","làm sao","như nào","thế nào","cái chi","gì","bao nhiêu","mấy","?"]
    for signal in list_question_signal:
        if signal in message.lower():
            print(signal)
            return True
    #bắt YES-NO/WH question mà signal cuối câu 
    if message.split(" ")[-1].lower()=="chưa" or message.split(" ")[-1].lower()=="vậy" or message.split(" ")[-1].lower()=="không" or message.split(" ")[-1].lower()=="ta" or message.split(" ")[-1].lower()=="sao":
        return True

    #bắt YES-NO question cuối câu có chủ ngữ
    list_question_signal_last=["vậy","chưa","không","sao"]
    list_subject=["bạn","cậu","ad","anh","chị"]
    for subject in list_subject:
        for question_signal_last in list_question_signal_last:
            if message.split(" ")[-1].lower()==subject and message.split(" ")[-2].lower()==question_signal_last:
                return True 
    return False

# print(check_question("sinh viên khoa máy tính được đi không bạn"))

