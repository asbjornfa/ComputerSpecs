import platform
import socket
import GPUtil
import cpuinfo
import psutil



class Computer:
    def __init__(self):
        self.hostname = socket.gethostname()
        self.system = platform.system()
        self.machine = platform.machine()
        self.kernel = platform.release()
        self.compiler = platform.python_compiler()
        self.processor = cpuinfo.get_cpu_info()['brand_raw']
        self.memory = round(psutil.virtual_memory().total / (1024 ** 3))
        self.disk = round(psutil.disk_usage('/').total / (1024 ** 3))
        self.gpu = GPUtil.getGPUs()
        self.ram_used = round(psutil.virtual_memory().used / (1024 ** 3))
        self.disk_used = round(psutil.disk_usage('/').used / (1024 ** 3))

    def print_specs(self):
        print("Hostname: %s" % self.hostname)
        print("System: %s" % self.system)
        print("Machine: %s" % self.machine)
        print("Kernel: %s" % self.kernel)
        print("Compiler: %s" % self.compiler)
        print("Processor: %s" % self.processor)
        print("Memory: %s" % self.memory + " GiB")
        print("Disk: %s" % self.disk + " GiB")
        print(" ")
        print("--- GPU ---")
        if not self.gpu:
            print("No GPU available")
        else:
            for gpus in self.gpu:
                print(f"GPU name: {gpus.name}")

        print(" ")
        print("--- RAM & Disk usage ---")
        print("RAM used: " + str(self.ram_used) + " GiB" + " / " + str(self.memory) + " GiB")
        print("Disk used: " + str(self.disk_used) + " GiB" + " / " + str(self.disk) + " GiB")





pcSpecs = Computer()
pcSpecs.print_specs()

