def send_email(message, recipient, sender="university.help@gmail.com"):
    valid_domains = [".com", ".ru", ".net"]
    recipient_valid = 0
    sender_valid = 0

    if recipient.find("@") > 0 and sender.find("@"):
        for i in valid_domains:
            if recipient.find(i) >= 0:
                recipient_valid += 1

        for y in valid_domains:
            if sender.find(y) >= 0:
                sender_valid += 1

        if recipient_valid == 0 or sender_valid == 0:
            print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        elif sender == recipient:
            print("Нельзя отправить письмо самому себе!")
        elif sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Пожалуйста, исправьте задание', 'urban.student.mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
