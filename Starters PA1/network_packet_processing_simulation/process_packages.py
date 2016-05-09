# python3

class Request:
    def __init__(self, arrival_time, process_time):
        self.arrival_time = arrival_time
        self.process_time = process_time

class Response:
    def __init__(self, dropped, start_time, process_time):
        self.dropped = dropped
        self.start_time = start_time #tine whn packet processing begins. this may happen later than arrival time
        self.end_time = start_time + process_time #time when packet process is complete. i.e. ready for dequeueing

class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time_ = []
        self.read = 0 #index of position that we'll read from
        self.write = 0 #index of position that we'll write to
        self.q = [None]*(self.size) #stores request objects.
        self.available_capacity = self.size
    def Enqueue(self, item):
        #first check if we have unused capacity
        if self.available_capacity > 0:
            self.available_capacity -= 1
            retval = True
            self.q[self.write] = item
            if self.write < self.size-1:
                self.write += 1
            else:
                self.write = 0
        else:
            retval = False
        #return retval #no need to return anything
        pass
    def Dequeue(self):
        if self.available_capacity < self.size:
            retval = self.q[self.read]
            self.q[self.read] = None
            self.available_capacity += 1
            if self.read < self.size-1:
                self.read += 1
            else:
                self.read = 0
        else:
            retval = None
        return retval
    def Top(self): #read oldest without dequeueing
        if self.available_capacity < self.size:
            retval = self.q[self.read]
        else:
            retval = None
        return retval
    def Bottom(self): #read newest entry without dequeueing
        if not self.Empty():
            retval = self.q[self.write-1]
        else:
            retval = None
        return retval
    def Empty(self):
        if self.available_capacity == self.size:
            return True
        else:
            return False
    def Full(self):
        if self.available_capacity == 0:
            return True
        else:
            return False
    def Show_stats(self):
        print("size: ", self.size)
        print("available_capacity: ", self.available_capacity)
        print("read pointer: ", self.read)
        print("write pointer: ", self.write)
        print("q: ", self.q)
    def Process(self, request): #this fn is called once per received packet, at the simulated time
        # write your code here
        #first check if at this "time" any "response" packets need to be dequeued
        current_time = request.arrival_time
        #print("processing req", request.arrival_time, request.process_time)
        while ( (not self.Empty()) and (self.Top().end_time <= current_time) ):
            last_res = self.Dequeue()
            #print("currtime is", current_time, "dequeued res", last_res.start_time, last_res.end_time)
        if not self.Full():
            if not self.Empty():
                bot_res = self.Bottom()
                #print("currtime is", current_time, "top res", bot_res.start_time, bot_res.end_time)
                start_time = bot_res.end_time
            else:
                start_time = request.arrival_time
            #end_time = start_time + request.process_time
            res = Response(False, start_time, request.process_time)
            #print("enqueing res. start_time=", start_time, "process_time=", request.process_time, "res_end_time", res.end_time)
            self.Enqueue(res)
            return res
        else:
            return Response(True, -1, 0) #buffer full, so discard packet
        

def ReadRequests(count):
    requests = []
    for i in range(count):
        arrival_time, process_time = map(int, input().strip().split())
        requests.append(Request(arrival_time, process_time))
    return requests

def ProcessRequests(requests, buffer):
    responses = []
    for request in requests:
        responses.append(buffer.Process(request))
    return responses

def PrintResponses(responses):
    for response in responses:
        print(response.start_time if not response.dropped else -1)

if __name__ == "__main__":
    size, count = map(int, input().strip().split())
    requests = ReadRequests(count)

    buffer = Buffer(size)
    responses = ProcessRequests(requests, buffer)

    PrintResponses(responses)
