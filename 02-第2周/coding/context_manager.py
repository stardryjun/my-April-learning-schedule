class MyContextManager:
    def __enter__(self):
        print("Entering the context")
        return self
    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting the context")
        if exc_type:
            print(f"An exception occurred: {exc_value}")
            return True  # Suppress the exception

with MyContextManager() as manager:
    open("non_existent_file.txt", "w")
    raise ValueError("This is a test exception")