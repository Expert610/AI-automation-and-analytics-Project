# 3. Create a Chat System using Object-Oriented Programming (OOP) concepts. (Marks 4)
# You need to create the following classes:
# • User
# • Message
# • ChatRoom
#  The system should implement the following functionalities:
# • Sending messages
# • Viewing chat history
# • User joining and leaving the chat room

class User:
    def __init__(self, name):
        self.name = name
    def send_message(self, chatroom, text):
        message = Message(self.name, text)
        chatroom.add_message(message)
class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text
    def display(self):
        print(f"{self.sender}: {self.text}")
class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []
    def join(self, user):
        self.users.append(user)
        print(f"{user.name} joined the chat.")
    def leave(self, user):
        self.users.remove(user)
        print(f"{user.name} left the chat.")
    def add_message(self, message):
        self.messages.append(message)
    def chat_history(self):
        print("\nChat History:")
        for message in self.messages:
            message.display()
room = ChatRoom("General")
user1 = User("Ali")
user2 = User("Sara")
room.join(user1)
room.join(user2)
user1.send_message(room, "Hello everyone!")
user2.send_message(room, "Hi Ali, how are you?")
user1.send_message(room, "I am doing great.")
room.chat_history()
room.leave(user2)