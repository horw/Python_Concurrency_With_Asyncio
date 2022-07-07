from asyncio import Future


my_future = Future()

print(f'Is my future done? {my_future.done()}')
print(f'What is result of my_future {my_future.result()}')

