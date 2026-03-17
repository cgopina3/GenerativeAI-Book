# Emoji Password Strength Checker
# Converts emojis to hex, splits into nibbles, and counts unique nibbles

def emoji_password_strength(password: str):
    hex_values = []

    for ch in password:
        hex_code = hex(ord(ch))[2:]  # Unicode → hex (remove 0x)
        hex_values.extend(hex_code)

    unique_nibbles = set(hex_values)
    entropy_score = len(unique_nibbles)

    print(f"Password: {password}")
    print(f"Hex nibbles: {hex_values}")
    print(f"Unique nibbles: {unique_nibbles}")
    print(f"Entropy score (unique nibbles): {entropy_score}")


if __name__ == "__main__":
    emoji_password = "🔒🔥🚀😀🐍"
    emoji_password_strength(emoji_password)
