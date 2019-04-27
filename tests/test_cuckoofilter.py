from cuckoopy import CuckooFilter
import  datetime

#读入文件
arr = []
with open('test.txt','r') as f:
    for i in range(0,900000):
        arr.append(f.readline())
f.close()

#申明CF

cf = CuckooFilter(capacity=999999, bucket_size=32, fingerprint_size=1)

for x in arr:
    cf.insert(str(x))
time2 = datetime.datetime.now()



look = []
for x in range(1,300000):
    look.append(arr[x])

time1 = datetime.datetime.now()
for k in look:
    cf.contains(k)
time2 = datetime.datetime.now()
print("the time is :", (time2-time1).total_seconds(),'s')



