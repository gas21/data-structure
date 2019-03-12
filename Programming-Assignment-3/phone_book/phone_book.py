# python3


class DummyPhoneBook:
    def __init__(self, queries):
        self.all_contacts = [None] * 10000000
        self.queries = queries

    def process_queries(self):
        for query in self.queries:
            if query[0] == "add":
                self.all_contacts[int(query[1])] = query[2]
            elif query[0] == 'del':
                self.all_contacts[int(query[1])] = None
            elif query[0] == 'find':
                print("not found") if self.all_contacts[(int(query[1]))] is None \
                    else print(self.all_contacts[(int(query[1]))])


if __name__ == '__main__':
    n = int(input())
    queries = [input().split() for i in range(n)]
    DPB = DummyPhoneBook(queries)
    DPB.process_queries()
