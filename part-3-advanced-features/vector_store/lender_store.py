class LenderStore:
    def __init__(self):
        self.store = []

    def add_lender(self, lender):
        self.store.append(lender)

    def retrieve_lenders(self, query):
        # Retrieve relevant lenders
        return [lender for lender in self.store if query in lender['name']]
