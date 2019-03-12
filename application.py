import os

from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit, join_room, leave_room
import json

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)


channel_list = {"Predvorje": [] }
present_channel = {"initial":"Predvorje"}

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":

        return render_template("index.html", channel_list=channel_list)

    elif request.method == "POST":
        channel = request.form.get("channel_name")
        user = request.form.get("username")

        # Dodavanje novog kanala
        if channel and (channel not in channel_list):
            channel_list[channel] = []
            return jsonify({"success": True})
        # Promijena kanala
        elif channel in channel_list:

            print(f"Switch to {channel}")
            present_channel[user] = channel
            channel_data = channel_list[present_channel[user]]
            return jsonify(channel_data)
        else:
            return jsonify({"success": False})
# kreiranje kanala
@socketio.on("create channel")
def create_channel(new_channel):
    emit("new channel", new_channel, broadcast=True)
# slanje poruka
@socketio.on("send message")
def send_message(message_data):
    channel = message_data["current_channel"]
    channel_message_count = len(channel_list[channel])
    del message_data["current_channel"]
    channel_list[channel].append(message_data)
    message_data["deleted_message"] = False
    if(channel_message_count >= 100):
        del channel_list[channel][0]
        message_data["deleted_message"] = True
    emit("recieve message", message_data, broadcast=True, room=channel)
# brisanje kanala
@socketio.on("Brisanje kanala")
def delete_channel(message_data):
    channel = message_data["current_channel"]
    user = message_data["user"]
    present_channel[user] = "Predvorje"
    del message_data["current_channel"]
    del channel_list[channel]
    channel_list["Predvorje"].append(message_data)
    message_data = {"data": channel_list["Predvvorje"], "deleted_channel": channel}
    emit("announce channel deletion", message_data, broadcast=True)
#izlazenje
@socketio.on("leave")
def on_leave(room_to_leave):
    print("Napustanje sobe")
    leave_room(room_to_leave)
    emit("Napustanje kanala", room=room_to_leave)
# pridruzivanje
@socketio.on("join")
def on_join(room_to_join):
    print("Pridruzivvanje sobi")
    join_room(room_to_join)
    emit("Pridruzivanje kanalu", room=room_to_join)