import subprocess

def main():
    data = subprocess.PIPE
    ping = subprocess.Popen(["ping", "google.com"], stdout=subprocess.PIPE,shell=True)
    ping.args = ['ping', 'youtube.com']
    print(type(ping))
    value, error = ping.communicate()
    # value2, error = ping.communicate()

    print(value.split(b"\n\r"))
    # print(value2)


class SystemCommander:
    def __init__(self, cmd):
        self._stdout_pipe = subprocess.PIPE
        self._stderr_pipe = subprocess.PIPE
        self._p_process: subprocess.Popen = subprocess.Popen(cmd)


if __name__ == "__main__":
    main()
