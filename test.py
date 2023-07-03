def twoOutOfThree(nums1, nums2, nums3):
    ls = list()
    res = list()
    hs1 = dict()
    hs2 = dict()
    hs3 = dict()
    for num in nums1:
        if num not in hs1:
            hs1[num] = 1
    for num in nums2:
        if num not in hs2:
            hs2[num] = 1
    for num in nums3:
        if num not in hs3:
            hs3[num] = 1
    # ls = [hs1,hs2,hs3]
    # ls.extend(hs1.keys())
    # ls.extend(hs2.keys())
    # ls.extend(hs3.keys())
    ls = list(hs1.keys()) + list(hs2.keys()) + list(hs3.keys())
    print(ls)
    # return ls

twoOutOfThree([1,1,3,2], [2,3], [3])