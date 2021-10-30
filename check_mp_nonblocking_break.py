import time

from ptools.mpython.omp_nb import OMPRunnerNB, RunningWorker


if __name__ == '__main__':

    class RWbreak(RunningWorker):
        def process(self, a):
           time.sleep(3)
           return f'done {a}'

    omp = OMPRunnerNB(rw_class=RWbreak, multiproc=5, verb=2)
    tasks = [{'a': f'task {ix}'} for ix in range(1000)]

    loop_ix = 0
    while True:

        if loop_ix == 15: break

        task = tasks.pop(0)
        omp.process(task)

        time.sleep(1)

        result = omp.get_result(block=False)
        if result:  print(f'loop_ix {loop_ix}, got result {result}')
        else:       print(f'loop_ix {loop_ix}, no result ready')

        loop_ix += 1

    omp.exit()