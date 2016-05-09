# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def get_hash(number):
    return number

def process_queries(queries):
    result = []
    # Keep list of all existing (i.e. not deleted yet) contacts.
    contacts = ["not found"]*(10**7) #creating a big list upfront, so we can index into any possible position
    for cur_query in queries:
        #whether query type is add or del or find, we need to find hash
        #in this case, hash function just returns the original number! i.e. direct addressing
        h = get_hash(cur_query.number)
        if cur_query.type == 'add':
            # if we already have contact with such number,
            # we should rewrite contact's name
            contacts[h] = cur_query.name
        elif cur_query.type == 'del':
            contacts[h] = "not found"
        else:
            #response = 'not found'
            #if contacts[h] != "not found":
            response = contacts[h]
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

