import time
from plyer import notification

def notify(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = 'E:\\Codaholic\\Videos\\Other videos\\Take a Break Notifier\\Warning icon.ico',
        timeout = 15
    )

if __name__ == "__main__":
    DUR = 2
    while True:
        time.sleep(60)
        notify('Let\'s take a break!', f'You have been using the computer for {DUR} hours! We recommend you to take a break to avoid strain oin your eyes!')
        DUR += 2
