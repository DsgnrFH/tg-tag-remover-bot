import requests

TOKEN = "TOKEN-HERE" # Token taken from BotFather goes here
API = f"https://api.telegram.org/bot{TOKEN}"
TAG = "meow" # Text to flag. In this example, bot will delete all the messages that contain "meow"
IGNORE_HUMANS = True # Only delete other bot's messages. Set to False to also include people (not recommended)
REACT_TO_MESSAGE = True # React with 👀 to non bots messages containing the tag, if ignoring humans

def react(chat_id, message_id, emoji="👀"):
    requests.post(f"{API}/setMessageReaction", json={
        "chat_id": chat_id,
        "message_id": message_id,
        "reaction": [{"type": "emoji", "emoji": emoji}],
    })

def main():
    offset = None
    while True:
        try:
            r = requests.get(f"{API}/getUpdates",
                             params={"offset": offset, "timeout": 1},
                             timeout=10).json()
        except requests.RequestException:
            continue

        for upd in r.get("result", []):
            offset = upd["update_id"] + 1
            msg = upd.get("message") or upd.get("channel_post")
            if not msg:
                continue

            sender = msg.get("from", {})
            text = msg.get("text", "") or msg.get("caption", "")

            if TAG not in text:
                continue

            # If another bot
            if IGNORE_HUMANS:
                if sender.get("is_bot"):
                    requests.post(f"{API}/deleteMessage", data={
                        "chat_id": msg["chat"]["id"],
                        "message_id": msg["message_id"],
                    })
                else if REACT_TO_MESSAGE:
                    react(msg["chat"]["id"], msg["message_id"])
            else:
                requests.post(f"{API}/deleteMessage", data={
                    "chat_id": msg["chat"]["id"],
                    "message_id": msg["message_id"],
                })

if __name__ == "__main__":
    main()
