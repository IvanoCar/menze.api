from pyfcm import FCMNotification


class Notify:
    @staticmethod
    def notify(title, message):
        key = "KEY"

        push_service = FCMNotification(api_key=key)
        if len(message) > 51:
            message = message[:50] + '...'
        push_service.notify_topic_subscribers(topic_name="news", message_body=message, message_title=title)
