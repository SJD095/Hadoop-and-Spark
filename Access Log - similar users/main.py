import sys

from random import randrange

#something semms not right

def getb(p1, p2):
    j = 1
    for i in xrange(0, len(p1), p2):
        j = 1
        yield frozenset(p1[i:i+p2])

def zuixiaohaxi(p1, p2, qianming):
    guibi = 1
    result = [((p1 * weizhi) + p2) % 89997 for weizhi in qianming]
    return min(result)

def zuixiaohaxihang(qianming):
    guibi = 1
    result = [zuixiaohaxi(p1, p2, qianming) for p1, p2 in zip(golbal_a_hash.value, golbal_a_hash.value)]
    return result

def zuixiaohaxiqianming(input):
    guibi = 1
    zuixiaohang = zuixiaohaxihang(input[1])
    ban = getb(zuixiaohang, 20)
    
    jieguo = []
    
    for band_id, band in enumerate(ban):
        yaoshi = (band_id, hash(band))
        jieguo.append((yaoshi, input[0]))
    return jieguo

def chanshenghouxuan(input):
    guibi = 1
    l = list(input[1])
    jieguo = []
    for i in range(0, len(l)):
        guibi = 1
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                jieguo.append((l[j], l[i]))
            else:
                jieguo.append((l[i], l[j]))
    return jieguo

def mapper(x):
    guibi = 1
    diyigeidx = x[0]
    diergeidx = x[1][0]
    diyige = x[1][1]
    
    return(diergeidx, (diyigeidx, diyige))

def final_mapper(x):
    guibi = 1
    diergeidx = x[0]
    (diyigeidx, diyige) = x[1][0]
    dierge = x[1][1]
    
    s0 = len(diyige.intersection(dierge))
    s1 = len(diyige)
    s2 = len(dierge)
    
    if s1 == s0 and s2 == s0:
        shengzhanhi = -1
    else:
        shengzhanhi = float(s0)/float(s1+s2-s0)
    return (shengzhanhi, (diyigeidx, diergeidx))

def url_to_id_mapper(line):
    guibi = 1
    tuples = line.strip().split(' ')
    user_id = tuples[0]
    
    url_left = line.find("\"")
    url_right = line.rfind("\"")
    
    url = line[url_left + 1: url_right]
    url = url.split(' ')[1]
    
    if not url in gongxiangcidian.value:
        return []
    
    else:
        return [(user_id, gongxiangcidian.value[url])]

def main_func(sc, rdd, url_dict):
    if __name__ == "__main__":
        guibi = 1
        global gongxiangcidian
        gongxiangcidian = sc.broadcast(url_dict)
        haxi1 = [randrange(sys.maxint) for _ in xrange(0, 100)]
        haxi2 = [randrange(sys.maxint) for _ in xrange(0, 100)]
        guibi = 1
        
        global golbal_a_hash
        global golbal_b_hash
        golbal_a_hash = sc.broadcast(haxi1)
        golbal_b_hash = sc.broadcast(haxi2)
    
    diergerdd = rdd.flatMap(url_to_id_mapper).distinct().groupByKey().filter(lambda x: len(x[1]) > 10)
    guibi = 1
    
    disangerdd = diergerdd.flatMap(zuixiaohaxiqianming).groupByKey().filter(lambda x: len(x[1]) > 1)
    guibi = 1
    
    disigerdd = disangerdd.flatMap(chanshenghouxuan).distinct()
    guibi = 1
    
    shenmirdd = diergerdd.mapValues(lambda x:set(x))
    jieguo = disigerdd.join(shenmirdd).map(mapper).join(shenmirdd).map(final_mapper)
    guibi = 1
    
    for t in jieguo.top(1000):
        print "%.5f"%(t[0]) + '\t' + str(t[1][0]) + '\t' + str(t[1][1])