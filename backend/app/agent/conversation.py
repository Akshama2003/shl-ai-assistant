def build_conversation(messages):

    conversation = []

    for message in messages:

        role = message.role.capitalize()

        conversation.append(
            f"{role}: {message.content}"
        )

    return "\n".join(conversation)