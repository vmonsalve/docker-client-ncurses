import subprocess

class RuntimeHandler:
    def __init__(self, name, match_fn, start_cmd, stop_cmd):
        self.name = name
        self.match_fn = match_fn
        self.start_cmd = start_cmd
        self.stop_cmd = stop_cmd

    def matches(self, socket_path):
        return self.match_fn(socket_path)

    def start(self):
        return self._run(self.start_cmd)

    def stop(self):
        return self._run(self.stop_cmd)

    def _run(self, command):
        try:
            subprocess.run(command, check=True)
            return True
        except subprocess.CalledProcessError as e:
            print(f"[{self.name}] Error: {' '.join(command)} → {e}")
            return False