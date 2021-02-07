import smtplib

MY_EMAIL = “SENDING EMAIL”
MAIN_EMAIL = “RECEIVING EMAIL”
PASSWORD = “SENDING EMAIL PASSWORD”

DAILY_TASKS = [
    "Have a good morning",
    "Stretch with ab roller and yoga mat",
    "Get 10+ minutes of fresh air",
    "Open Fold app",
    "Trade stocks",
    "Monitor options contracts",
    "Track trades",
    "Study Japanese with Tobira textbook",
    "Do Anki flash cards",
    "Workout at the gym",
    "Read",
    "Count macros",
    "Journal",
    "Sleep well"
]

tasks = ""
for _ in range(0, len(DAILY_TASKS)):
    tasks += (str(_ + 1) + ". " + DAILY_TASKS[_] + "\n")

with smtplib.SMTP("smtp.gmail.com", 587) as connection:
    connection.starttls()  # way of securing the connection to the email server
    connection.login(user=MY_EMAIL, password=PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MAIN_EMAIL,
        msg=f"Subject:Daily Tasks for today\n\n{tasks}"
    )
