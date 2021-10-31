import random
import time

from ptools.lipytools.little_methods import prob
from ptools.mpython.omp_nb import OMPRunnerNB, RunningWorker, MultiprocParam


def demo_nb(
        task_prob=                  0.7,
        multiproc: MultiprocParam=  5,
        ordered_results=            False,
        num_loops=                  20):

    # prepares task for given int
    def get_task(ix: int): return {'a': f'task {ix}'}

    # task worker
    class RWbreak(RunningWorker):
        def process(self, a):
           time.sleep(random.randint(1,5))
           return f'done {a}'

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

        task = get_task(task_ix) if prob(task_prob) else None
        if task:
            print(f' > got new task to process')
            omp.process(task)
            task_ix += 1

        result = omp.get_result(block=False)
        if result:  print(f' > got result: {result}')
        else:       print(f' > no result ready')

        time.sleep(1)
        loop_ix += 1

    omp.exit()


if __name__ == '__main__':

    demo_nb()