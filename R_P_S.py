def f_emoji(massage):
    emoji = {
        ":)": "😁",
        ":(": "🙁"
    }
    words = message.split()
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output

message = input(">")
result = f_emoji(message)
print(result)