import numpy as np
import random
import time

from ptools.lipytools.little_methods import prob
from ptools.mpython.omp_nb import OMPRunnerNB, RunningWorker, MultiprocParam


def demo_nb(
        multiproc: MultiprocParam=  72,
        ordered_results=            True,
        num_loops=                  200):

    # prepares task for given int
    def get_task(ix: int): return {'name': f'task {ix}', 'array':np.random.random((100,100))}

    # task worker
    class RWbreak(RunningWorker):
        def process(self, name, array):
           array = np.transpose(array)
           return {'info':f'done {name}', 'array':array}

    omp = OMPRunnerNB(
        rw_class=           RWbreak,
        multiproc=          multiproc,
        ordered_results=    ordered_results,
        verb=               1)

    loop_ix = 0
    task_ix = 0
    while True:
        print(f'\nLoop_ix: {loop_ix}')

        if loop_ix == num_loops: break

        n_tasks = 0
        for _ in range(random.randint(1,10)):
            task = get_task(task_ix)
            omp.process(task)
            task_ix += 1
            n_tasks += 1
        print(f' > sent {n_tasks} tasks')

        n_results = 0
        while True:
            result = omp.get_result(block=False)
            if result is not None: n_results += 1
            else: break
        print(f' > received {n_results} results')

        loop_ix += 1

    omp.exit()


if __name__ == '__main__':

    demo_nb()