# multiprocessing accessible data, np.array wont explode RAM usage by processes in contrast to list or dict, but is very sensitive to sentence length (long sentences will explode mem usage @np.array)
class MPData:

    def __init__(
            self,
            fileFP=     None,   # full path to file with text lines
            data=       None,   # data in form of iterable (list, dict, etc)
            name=       'MPData',
            verb=       0):

        self.verb =verb
        self.name = name

        self.len, self.data = 0, None

        new_data = data
        if fileFP:
            if self.verb > 0: print('\n%s loading file data...' % self.name)
            with open(fileFP, 'r') as file:
                new_data = [line[:-1] for line in file]

        self.len = len(new_data)
        self.data = np.asarray(new_data)

        print(self.data.shape)
        print(self.data.dtype)

        if self.verb > 0: print('\n%s got %d (%s) lines of data' % (self.name, self.len, short_scin(self.len)))

    # returns line indexed with num from data
    def get_data(
            self,
            num=    None):      # None returns random

        if num is None: num = np.random.randint(self.len)
        if num < self.len: return self.data[num]
        return None
