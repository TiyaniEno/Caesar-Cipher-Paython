# cipher.py
# Encodes messages using a Caesar cipher with a shift of 15


def encode_message(message):
    """
    Encodes a message by shifting each letter 15 places forward.
    Keeps spaces and punctuation unchanged.
    """

    encoded = ""

    for char in message:

        # Handle lowercase letters
        if 'a' <= char <= 'z':
            shifted = ((ord(char) - ord('a') + 15) % 26) + ord('a')
            encoded += chr(shifted)

        # Handle uppercase letters
        elif 'A' <= char <= 'Z':
            shifted = ((ord(char) - ord('A') + 15) % 26) + ord('A')
            encoded += chr(shifted)

        # Keep spaces and punctuation unchanged
        else:
            encoded += char

    return encoded


# Main program loop
while True:

    # Ask user for input
    message = input("\nEnter a message to encode (or type 'exit' to quit): ")

    # Exit option
    if message.lower() == "exit":
        print("Program closed.")
        break

    # Validate empty input
    if message.strip() == "":
        print("Error: Please enter a message.")
        continue

    # Encode and print result
    encoded_message = encode_message(message)

    print("Encoded message:", encoded_message)
