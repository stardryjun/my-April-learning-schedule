from contextlib import contextmanager

@contextmanager
def my_context_manager():
    print("Entering the context")
    try:
        yield
    except Exception as e:
        print(f"An exception occurred: {e}")
    finally:
        print("Exiting the context")

with my_context_manager():
    print("Inside the context")
    raise ValueError("This is a test exception")