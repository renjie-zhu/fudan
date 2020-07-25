#!/usr/bin/python3
import random
import math
"""
O(log(m+n))
"""
def findMedianSortedArrays(nums1, nums2) :
  def findKthNum(k) :
    index1 = 0
    index2 = 0
    while True:
      if index1 == m :
        return nums2[index2 + k-1]
      if index2 == n :
        return nums1[index1 + k-1]
      if k == 1 :
        return min(nums1[index1], nums2[index2])
      newindex1 = min(index1 + (k//2) -1, m-1)
      newindex2 = min(index2 + (k//2) -1, n-1)
      print ("index1:%d index2:%d\n newindex1:%d newindex2:%d\nk:%d" % (index1, index2, newindex1, newindex2, k))
      pivot1 = nums1[newindex1]
      pivot2 = nums2[newindex2]
      if pivot1 <= pivot2 :
        k = k - (newindex1 - index1) - 1
        index1 = newindex1 + 1
        print ("pivot1 <= pivot2 k:%d index1:%d index2:%d\n" % (k, index1, index2))
      elif pivot1 >  pivot2 :
        k = k - (newindex2 - index2) - 1
        index2 = newindex2 + 1
        print ("pivot1 >  pivot2 k:%d index1:%d index2:%d\n" % (k, index1, index2))
  m = len(nums1)
  n = len(nums2)
  if (m+n)%2 == 1 :
    result2 = findKthNum((m + n) // 2 + 1)
    return result2
  else :
    result2 = (findKthNum((m + n) // 2) + findKthNum((m + n) // 2 + 1) ) / 2
    return result2

def sort_for_test(list1, list2):
  result1 = 0.0
  list3 = []
  list1.sort()
  list2.sort()
  for i in list1:
    list3.append(i)
  for j in list2:
    list3.append(j)
  list3.sort()
  print (list1) 
  print (list2)
  print (list3)
  list3_length = len(list3)
  if (list3_length % 2 == 1) :
    result1 = list3[list3_length // 2]
  else :
    result1 = (list3[list3_length // 2 - 1] + list3[list3_length // 2]) / 2
  return result1

if __name__ == "__main__" :
  for i in range(100000) :
    l1 = []
    l2 = []
    for i in range(random.randint(1,20)) :
      l1.append(random.randint(1,20))
    for i in range(random.randint(0,21)) :
      l2.append(random.randint(0,20))
    result1 = sort_for_test(l1, l2)
    result2 = findMedianSortedArrays(l1, l2)
    print ("result1:%f, result2:%f\n" % (result1, result2))
    if not math.isclose(result1, result2) :
      print ("Error!!")
      break
