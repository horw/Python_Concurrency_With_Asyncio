import asyncio
import concurrent.futures
import functools
import time
from typing import List, Dict
freqs = {}


def partition(data: List, chunk_size: int) -> List:
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def map_frequencies(chunk: List[str]) -> Dict[str,int]:
    counter = {}
    for line in chunk:
        word, _, count, _ = line.split('\t')
        if counter.get(word):
            counter[word] = counter[word] + int(count)
        else:
            counter[word] = int(count)
    return counter


def merge_dictionaries(first:Dict[str, int],
                       second: Dict[str,int]) -> Dict[str,int]:
    merged = first
    for key in second:
        if key in merged:
            merged[key] = merged[key] + second[key]
        else:
            merged[key] = second[key]
    return merged


async def listing_(partion_size: int):
    with open('googlebooks-eng-all-1gram-20120701-a', encoding='utf-8') as f:
        #listing6_7
        if False:
            lines = f.readlines()
            start = time.time()

            for line in lines:
                data = line.split('\t')
                word = data[0]
                count = int(data[2])
                if word in freqs:
                    freqs[word]= freqs[word] + count
                else:
                    freqs[word] = count

            end = time.time()
            print(f'{end-start:.4f}')
        else:
            contents = f.readlines()
            loop = asyncio.get_event_loop()
            tasks = []
            start = time.time()
            with concurrent.futures.ProcessPoolExecutor() as pool:
                for chunk in partition(contents, partion_size):
                    tasks.append(loop.run_in_executor(pool,
                                                      functools.partial(map_frequencies, chunk)))
                intermediate_result = await asyncio.gather(*tasks)
                final_result = functools.reduce(merge_dictionaries, intermediate_result)
                print(f"Aardvark has appeared {final_result['Aardvark']} times.")

                end = time.time()
                print(f'MapReduce took: {(end-start):.4f} seconds')
