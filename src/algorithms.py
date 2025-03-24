import numpy as np


def k_th(body, k, remove_i=True):

    nove_body = []
    if remove_i:
        for i in range(0, len(body), k):
            nove_body.append(body[i])
    else:
        nove_body.append(body[0])
        for i in range(1, len(body)):
            if i % k != 0:
                nove_body.append(body[i])

    if nove_body[-1] != body[-1]:
        nove_body.append(body[-1])

    return nove_body


def find_maximum(body):
    A = np.array(body[0])
    B = np.array(body[-1])
    maximum = 0
    index = 0
    dist = 0
    pole = []
    for i in range(1, len(body) - 1):
        C = np.array(body[i])

        t = np.dot(B - A, C - A) / (np.dot(B - A, B - A))
        P = A + t * (B - A)

        dist = (float((P[0] - C[0])) ** 2 + float((P[1] - C[1])) ** 2) ** 0.5
        if t < 0 or t > 1:
            dist = min(float((A[0]-C[0]))**2 + float((A[1] - C[1]))**2, float((B[0]-C[0]))**2 + float((B[1] - C[1]))**2)
        if dist > maximum:
            pole = [A, B, C, P]
            maximum = dist
            index = i
    # print(pole)
    return index, maximum


def osa(body, k):
    global ukazatele
    global delka_osy
    ukazatele = np.array([False] * len(body))
    ukazatele[0], ukazatele[-1] = True, True
    nove_body = []
    A = body[0]
    B = body[-1]
    delka_osy = ((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2) ** 0.5

    splits = [(body, ukazatele)]
    for _ in range(k):
        maxx = 0
        idx = (-1, -1)
        for i in range(len(splits)):
            index, dist = find_maximum(splits[i][0])
            if dist > maxx:
                maxx = dist
                idx = (i, index)
        splits[idx[0]][1][idx[1]] = True
        new_splits = [
            splits[: idx[0]],
            [
                ((splits[idx[0]][0][: idx[1] + 1]), (splits[idx[0]][1][: idx[1] + 1])),
                ((splits[idx[0]][0][idx[1] :]), (splits[idx[0]][1][idx[1] :])),
            ],
            splits[idx[0] + 1 :],
        ]
        
        splits = [x for l in new_splits for x in l]

    for i in range(len(body)):
        if ukazatele[i]:
            nove_body.append(body[i])
    return nove_body


def angles(points, k):
    pnts = np.array(points)
    ins = pnts[2:, :] - pnts[1:-1, :]
    outs = pnts[:-2, :] - pnts[1:-1, :]

    # cos(alpha) = u.dot(v) / (sqrt(u.dot(u)) * sqrt(v.dot(v)))
    cos_a = np.array(
        [
            ins[i, :].dot(outs[i, :])
            / (np.sqrt(ins[i, :].dot(ins[i, :])) * np.sqrt(outs[i, :].dot(outs[i, :])))
            for i in range(len(ins))
        ]
    )
    cos_ind = np.argsort(cos_a)

    res = np.concatenate(
        ([pnts[0]], pnts[1:-1][np.sort(cos_ind[len(points) - k + 1 :]), :], [pnts[-1]])
    )
    return [(res[i, 0], res[i, 1]) for i in range(res.shape[0])]


def distance(points, k):
    pnts = np.array(points)
    ins = pnts[2:, :] - pnts[1:-1, :]
    outs = pnts[:-2, :] - pnts[1:-1, :]

    dists = [
        [np.sqrt(ins[i].dot(ins[i])), np.sqrt(outs[i].dot(outs[i]))]
        for i in range(len(ins))
    ]
    # random numpy hack for sorting
    s_dists = np.array(
        [tuple(sorted(p)) for p in dists], dtype=[("x", "<f16"), ("y", "<f16")]
    )
    ind = np.argsort(s_dists, axis=0, order=["x", "y"])

    res = np.concatenate(([pnts[0]], pnts[1:-1][np.sort(ind[len(points) - k + 1 :]), :], [pnts[-1]]))

    return [(res[i, 0], res[i, 1]) for i in range(res.shape[0])]
