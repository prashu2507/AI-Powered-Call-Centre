class ConversationStore:
    def __init__(self):
        self.store = []

    def add_conversation(self, conversation):
        self.store.append(conversation)

    def retrieve_conversations(self, query):
        # Retrieve relevant conversations
        return [conv for conv in self.store if query in conv]
