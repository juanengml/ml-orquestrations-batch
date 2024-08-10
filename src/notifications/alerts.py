import requests
import os


class Alert:
    def __init__(self):
        
        self.webhook_url = os.getenv('WEBHOOK_URL')

    def send_alert(self, title, message, image_url, service_name, pipeline_name, alert_type):
        color_map = {
            'Success': 3066993,  # Green
            'Info': 3447003,     # Blue
            'Warning': 15105570  # Yellow
        }

        payload = {
            "username": f"{service_name} - {pipeline_name}",
            "embeds": [
                {
                    "title": title,
                    "description": message,
                    "color": color_map.get(alert_type, 3447003),  # Default to Info color if type not found
                    "image": {"url": image_url},
                }
            ]
        }

        response = requests.post(self.webhook_url, json=payload)
        if response.status_code != 204:
            raise Exception(f"Failed to send alert: {response.status_code}, {response.text}")

class Success(Alert):
    def __init__(self):
        super().__init__()

    def send(self, title, message, image_url, service_name, pipeline_name):
        self.send_alert(title, message, image_url, service_name, pipeline_name, 'Success')


class Info(Alert):
    def __init__(self):
        super().__init__()

    def send(self, title, message, image_url, service_name, pipeline_name):
        self.send_alert(title, message, image_url, service_name, pipeline_name, 'Info')


class Warning(Alert):
    def __init__(self):
        super().__init__()

    def send(self, title, message, image_url, service_name, pipeline_name):
        self.send_alert(title, message, image_url, service_name, pipeline_name, 'Warning')


def main():
    # Exemplo de uso
    webhook_url = os.getenv('WEBHOOK_URL')

    success_alert = Success(webhook_url)
    success_alert.send(
        title="Deploy Success",
        message="The deployment completed successfully.",
        image_url="https://i.pinimg.com/originals/43/bc/8b/43bc8b3aa3a3f59d1bfcf3779f615bb3.png",
        service_name="MyService",
        pipeline_name="CI/CD Pipeline"
    )

    info_alert = Info(webhook_url)
    info_alert.send(
        title="Information",
        message="The pipeline is running as expected.",
        image_url="https://i.pinimg.com/originals/43/bc/8b/43bc8b3aa3a3f59d1bfcf3779f615bb3.png",
        service_name="MyService",
        pipeline_name="CI/CD Pipeline"
    )

    warning_alert = Warning(webhook_url)
    warning_alert.send(
        title="Warning",
        message="There was a minor issue during deployment.",
        image_url="https://i.pinimg.com/originals/43/bc/8b/43bc8b3aa3a3f59d1bfcf3779f615bb3.png",
        service_name="MyService",
        pipeline_name="CI/CD Pipeline"
    )
if __name__ == "__main__":
    main()