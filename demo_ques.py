from multiprocessing import Queue, Pipe
import numpy as np
import pickle
from tqdm import tqdm


def put_get_que(que, tasks):
    print(f'putting {len(tasks)} tasks of size {len(pickle.dumps(tasks[0]))} bytes on que ..')
    for t in tqdm(tasks): que.put(t)
    print('receiving tasks...')
    for _ in tqdm(tasks): g = que.get()


def put_get_pipe(po,pi, tasks):
    print(f'p/r {len(tasks)} tasks of size {len(pickle.dumps(tasks[0]))} bytes with pipe ..')
    for t in tqdm(tasks):
        pi.send(t)
        g = po.recv()


def qp_tests():

    print(type(Queue))
    que = Queue()
    print(type(que))

    po, pi = Pipe()

    #tasks = ['asdfas' for _ in range(int(1e5))]
    #put_get(que,tasks)

    #tasks = [['asdfas' for _ in range(1000)] for _ in range(int(1e5))]
    #put_get(que, tasks)

    tasks = [np.random.random(1000)] * int(1e5)
    put_get_que(que, tasks)
    put_get_pipe(po,pi, tasks)


if __name__ == '__main__':
    qp_tests()






