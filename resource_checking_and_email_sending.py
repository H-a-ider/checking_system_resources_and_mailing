import psutil
import smtplib

sender = ''
receivers = ''

message = []

cpu_usage = psutil.cpu_percent(interval=1)
memory_usage = psutil.virtual_memory().percent
disk_usage = psutil.disk_usage('/').percent

for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(proc.info)

if cpu_usage > 80:
    message.append(f"Alert! CPU usage is high {cpu_usage}")
if memory_usage > 80:
    message.append(f"Alert! Memory usage is high {memory_usage}")
if disk_usage > 80:
    message.append(f"Alert! Disk usage is high {disk_usage}")

try:
    smtpObj = smtplib.SMTP('localhost')
    subject = "System Health Alert"
    body = '\n'.join(message)
    msg = f'Subject: {subject}\n{body}'
    smtpObj.sendmail(sender, receivers, msg)
    print("Successfully sent email")
except smtplib.SMTPException as e:
    print(f"Error: unable to send email - {e}")

print("\n")
print(f"CPU Usage: {cpu_usage}%")
print("\n")
print(f"Memory Usage: {memory_usage}%")
print("\n")
print(f"Disk Usage: {disk_usage}%")
print("\n")
print(message)
