"""
Завдання 4 (необов'язкове завдання)
Реалізуйте структуру даних для системи коментарів так, щоб коментарі могли мати відповіді, які, в свою чергу, також могли мати відповіді, формуючи таким чином ієрархічну структуру.
Також візьміть до уваги наступні вимоги:
Реалізуйте клас Comment, що представляє собою окремий коментар. Він має зберігати текст коментаря, автора та список відповідей.
Метод класу add_reply має додавати нову відповідь до коментаря.
Метод класу remove_reply має видаляти відповідь із коментаря. Це має змінювати текст коментаря на стандартне повідомлення (наприклад, "Цей коментар було видалено.") і встановлювати прапорець is_deleted в True.
Метод display має рекурсивно виводити коментар та всі його відповіді, використовуючи відступи для відображення ієрархічної структури.
"""
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = "   " * level
        print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

if __name__ == "__main__":
    root_comment = Comment("Коментар 1", "Автор 1")
    reply1 = Comment("Відповідь 1", "Автор 2")
    reply2 = Comment("Відповідь 2", "Автор 3")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Відповідь 1.1", "Автор 4")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()
    root_comment.display()


