import math

data = {
    'Ace': [False, True, True, True],
    'Ten': [False, False, True, True],
    'FMv': [False, True, False, True]
}
play = ['stand', 'stand', 'hit', 'hit']

def entropy(pos, neg):
  P_pos = pos / float(pos + neg)
  P_neg = neg / float(pos + neg)
  if P_pos == 0:
    term1 = 0
  else:
    term1 = -P_pos * math.log(P_pos, 2.0)
  if P_neg == 0:
    term2 = 0
  else:
    term2 = -P_neg * math.log(P_neg, 2.0)
  return term1 + term2

def gain(pos, neg, splits):
    start = entropy(pos, neg)
    print('before entropy', start)
    msum = start
    for feature_val in splits:
        print('feature val', feature_val)
        size = (feature_val[0] + feature_val[1]) / (pos + neg)
        feature_entropy = entropy(feature_val[0], feature_val[1])
        msum -= size * feature_entropy
    return msum
    
# def sumEntropy(vector, play):
vector = data['Ace']
msum = 0
playdict = dict()
feature = list(zip(vector, play))
print(feature)
for k, v in feature:
    if k not in playdict:
        playdict[k] = dict()
        playdict[k][v] = 1
    else:
        tmp = playdict[k]
        tmp[v] = tmp.get(v, 1) if v not in tmp else tmp[v] + 1

print(f"play dict: {playdict}")

feature_dict = {}
for i in vector:
    feature_dict[i] = 1 if i not in feature_dict else feature_dict[i] + 1
    
print(f"feature dict: {feature_dict}")

def secTerm(featr_state, play_state, vector, pos, neg):
    return featr_state / len(vector) * entropy(pos, neg)

for k in playdict:
    fstate = playdict[k]
    print(k, sum(fstate.values()))


