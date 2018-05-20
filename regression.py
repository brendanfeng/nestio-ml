import tempfile
import subprocess

log_dir = tempfile.mkdtemp()
print("tensorbord-dir", log_dir)
subprocess.Popen(['pkill', '-f', 'tensorboard'])
subprocess.Popen(['tensorboard', '--logdir', log_dir])