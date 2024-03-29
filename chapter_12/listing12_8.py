import asyncio
from asyncio import Queue, PriorityQueue
from dataclasses import dataclass, field


@dataclass(order=True)
class WorkItem:
    priority: int
    data:str = field(compare=False)


async def worker(queue: Queue):
    while not queue.empty():
        work_item: WorkItem = await queue.get()
        print(f'Processing work item {work_item}')
        queue.task_done()


async def main():
    priority_queue = PriorityQueue()
    work_item =[
        WorkItem(3, 'Lowest priority'),
        WorkItem(3, 'Lowest priority second'),
        WorkItem(3, 'Lowest priority third'),
        WorkItem(2, 'Medium priority'),
        WorkItem(1, 'High priority'),
    ]
    worker_task = asyncio.create_task(worker(priority_queue))

    for work in work_item:
        priority_queue.put_nowait(work)

    await asyncio.gather(worker_task, priority_queue.join())


asyncio.get_event_loop().run_until_complete(main())