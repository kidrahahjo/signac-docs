# project.py
from flow import FlowProject


@FlowProject.operation
def compute_volume(job):
    volume = job.sp.N * job.sp.kT / job.sp.p
    with open(job.fn('volume.txt'), 'w') as file:
        file.write(str(volume) + '\n')


if __name__ == '__main__':
    FlowProject().main()
