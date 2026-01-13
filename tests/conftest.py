def pytest_sessionfinish(session, exitstatus):
    if exitstatus == 0:
        with open("example.txt", "w") as f:
            f.write("CI pipeline processed project successfully\n")
