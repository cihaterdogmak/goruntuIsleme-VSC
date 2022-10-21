# from dicFonctions import dicCreate , matrisContentsCalc

def dicCreate() :
    dic =  {}
    for i in range(256) :
        dic[i] = 0
    return dic

def matrisContentsCalc(mat,dic) :
    for i in range(0,len(mat)) :
        for j in range(0,len(mat[0])) :
            pix = mat[i][j]
            dic[pix] += 1
    return dic
