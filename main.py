import platform
import socket
import cpuinfo
import psutil

def pcInformation():
    #method calls
    hostname = socket.gethostname()
    system = platform.system()
    machine = platform.machine()
    kernel = platform.release()
    compiler = platform.python_compiler()
    processor = cpuinfo.get_cpu_info()['brand_raw']

    #Ram and disk methods + calculating to GiB
    ram_total = round(psutil.virtual_memory().total / (1024 ** 3))
    disk_total = round(psutil.disk_usage("/").total / (1024 ** 3))

    ram_used = round(psutil.virtual_memory().used / (1024 ** 3))
    disk_used = round(psutil.disk_usage("/").used / (1024 ** 3))

    ram_percentage = psutil.virtual_memory().used / psutil.virtual_memory().total * 100
    disk_percentage = psutil.disk_usage("/").used / psutil.disk_usage("/").total * 100

    #print statements
    print("")
    print("--- System Information ---")
    print("Hostname: " + hostname)
    print("System: " + system + " " + machine)
    print("Kernel: " + kernel)
    print("Compiler: " + compiler)
    print("Processor: " + processor)
    print("Memory: " + str(ram_total) + " GiB")
    print("Disk: " + str(disk_total) + " GiB")
    print("")
    print("--- GPU ---")
    print("No information")
    print("")
    print("--- RAM & Disk usage ---")
    print("RAM used: " + str(ram_used) + " GiB" + " / " + str(ram_total) + " GiB " + "(" + str(ram_percentage) + "%)")
    print("Disk used: " + str(disk_used) + " GiB" " / " + str(disk_total) + " GiB " + "(" + str(disk_percentage) + "%)")
    print("")

pcInformation()






