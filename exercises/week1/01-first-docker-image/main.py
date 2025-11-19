import os, socket, sys, json

def get_info():
    return {
        "hostname": socket.gethostname(),
        "pid": os.getpid(),
        "python_version": sys.version,
    }

if __name__ == "__main__":
    print(json.dumps(get_info(), indent=2))

