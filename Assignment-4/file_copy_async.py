import shutil
import threading
import time

start_time = time.perf_counter()

destination = './destination-files-async'
t1 = threading.Thread(target=shutil.copy, args=['./source-files/file1.zip', destination])
t2 = threading.Thread(target=shutil.copy, args=['./source-files/file2.zip', destination])
t3 = threading.Thread(target=shutil.copy, args=['./source-files/file3.zip', destination])
t4 = threading.Thread(target=shutil.copy, args=['./source-files/file4.zip', destination])

t1.start()
print('file 1 started copying')
t2.start()
print('file 2 started copying')
t3.start()
print('file 3 started copying')
t4.start()
print('file 4 started copying')

end_time = time.perf_counter()

total_time = end_time - start_time

print('Files are copying asynchronously. Time taken: ' + str(total_time))