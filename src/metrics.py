import numpy as np


def obsah(body,nove_body):
    obsah_puvodni = 0
    obsah_novy = 0
    n = len(body)
    for i in range(n):
        obsah_puvodni += 0.5*(body[i%n][0]*body[(i+1)%n][1] - body[i%n][1]*body[(i+1)%n][0])

    obsah_puvodni = abs(obsah_puvodni)
    n = len(nove_body)
    for i in range(n):
        obsah_novy += 0.5*(body[i%n][0]*body[(i+1)%n][1] - body[i%n][1]*body[(i+1)%n][0])
    obsah_novy = abs(obsah_novy)

    delta = abs(obsah_novy - obsah_puvodni)
    return (delta)


def MSE(body,nove_body):
    j = 0
    MSE = 0
    for i in range(len(nove_body)):
        while nove_body[i] != body[j%len(body)] and j < len(body):
            A = np.array(nove_body[i])
            B = np.array(nove_body[(i-1 + len(nove_body))%len(nove_body)])
            C = np.array(body[j])

            t = np.dot(B-A,C-A)/(np.dot(B-A,B-A))
            P = A + t*(B-A)

            dist = float((P[0]-C[0]))**2 + float((P[1] - C[1]))**2
            if t < 0 or t > 1:
                dist = min(float((A[0]-C[0]))**2 + float((A[1] - C[1]))**2, float((B[0]-C[0]))**2 + float((B[1] - C[1]))**2)
            MSE += dist
            #print(dist**0.5)
            j+=1
        #print("Bodu", i, "odpovídá bod:", j)
    return MSE/len(body)

def koncentrace():
    pass
