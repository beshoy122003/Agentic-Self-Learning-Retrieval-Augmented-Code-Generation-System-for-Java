class ConversationMemory:

    def __init__(self):

        self.history = []

    def add(self, user_query, response):

        self.history.append({
            "user": user_query,
            "assistant": response
        })

    def get_context(self, limit=3):

        return self.history[-limit:]


memory = ConversationMemory()