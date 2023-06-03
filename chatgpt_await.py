import time

async def fetch_data(url):
    print(f"Fetching data from {url}")
    # Simulate an I/O operation
    await sleep(2)
    print(f"Data fetched from {url}")

async def sleep(delay):
    # A simple implementation of sleep using time.sleep()
    awaitable = asyncio.sleep(delay)
    await awaitable

async def main():
    tasks = [
        fetch_data("https://api.example.com/data"),
        fetch_data("https://api.example.com/other-data"),
    ]
    # Wait for all tasks to complete
    await gather(*tasks)

# Define a simple gather function to await multiple tasks
async def gather(*coroutines):
    awaitables = [coro for coro in coroutines]
    while awaitables:
        done, awaitables = await wait(awaitables)

# Define a simple wait function to check the status of awaitables
async def wait(awaitables):
    done, pending = [], []
    for awaitable in awaitables:
        try:
            awaitable.send(None)
            done.append(awaitable)
        except StopIteration:
            pass
        else:
            pending.append(awaitable)
    return done, pending

# Run the main function
await main()
