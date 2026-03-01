class Notification:
    def send_message(self):
        print("Sending notification...")


class EmailNotification(Notification):
    def send_message(self):
        print("Sending notification via Email.")


class SMSNotification(Notification):
    def send_message(self):
        print("Sending notification via SMS.")


class AppNotification(Notification):
    def send_message(self):
        print("Sending notification via App.")


notifications = [EmailNotification(), SMSNotification(), AppNotification()]

for notification in notifications:
    notification.send_message()