import json
game_state = {
    "position": {
        "x": 100,
        "y": 200
    }
}

game_state["full_name"] = "Hello world"
game_state["enemy"] = {
    "x": 200,
    "y": 300
}

f = open("output.txt", "w")
f.write(json.dumps(game_state))
f.close()