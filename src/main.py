import show
import algorithms
import metrics
import sys

sys.setrecursionlimit(100000)

body = []
filename = input("Enter filename: ")
file = open(f'../geo dataset/{filename}',"r")
for line in file:
    line = line.split()
    body.append((float(line[0]),float(line[1])))
#print(body)
algo = input("Choose algorithm (0 = k-th points, 1 = angles, 2 = distance, 3 = min MSE): ")
reduce_by_in = input("Reduce points by: ")
reduce_by = int(reduce_by_in)
nove_body_osa = algorithms.osa(body,len(body)//reduce_by)
nove_body_kth = algorithms.k_th(body, reduce_by)
nove_body_angles = algorithms.angles(body, len(body)//reduce_by)
nove_body_distance = algorithms.distance(body, len(body)//reduce_by)
print(f"{metrics.MSE(body,nove_body_kth) / metrics.MSE(body,nove_body_osa) * 100:2f}%")
print(f"{metrics.MSE(body,nove_body_angles) / metrics.MSE(body,nove_body_osa) * 100:2f}%")
print(f"{metrics.MSE(body,nove_body_distance) / metrics.MSE(body,nove_body_osa) * 100:2f}%")
if algo == "0":
    show.vykresli_body(body,nove_body_kth,False,file=filename[:-5])
if algo == "1":
    show.vykresli_body(body,nove_body_angles,False,file=filename[:-5])
if algo == "2":
    show.vykresli_body(body,nove_body_distance,False,file=filename[:-5])
if algo == "3":
    show.vykresli_body(body,nove_body_osa,False,file=filename[:-5])
