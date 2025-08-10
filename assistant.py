import datetime
import wikipedia
import webbrowser

def handle_command(command):
    command = command.lower()

    if "time" in command:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"

    elif "tell me about" in command:
        topic = command.replace("tell me about", "").strip()
        try:
            summary = wikipedia.summary(topic, sentences=2)
            return summary
        except:
            return "Sorry, I couldn't find information on that topic."

    elif "open" in command:
        site = command.replace("open", "").strip()
        url = f"https://{site}.com"
        webbrowser.open(url)
        return f"Opening {site}..."

    else:
        return "Sorry, I didn't understand that command."