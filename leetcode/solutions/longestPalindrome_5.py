#!/home/xnli/tools/python3.6/bin/python3.6
#!/usr/bin/python3
import random
import string
"""
  k 
j x 0 1 2 3 4 5
  0 T
  1   T
  2     T
  3       T
  4         T
  5           T
"""
def longestPalindrome(str1): #dynamic programming
  n = len(str1)
  dp = [[False] * n for _ in range(n)]
  for i in range(n):
    dp[i][i] = True

  max_len = 1
  ans = ""
  for k in range(1, n):
    for j in range(k):
      if (str1[j] == str1[k] and (k - j < 3 or dp[j+1][k-1])):
        dp[j][k] = True
        new_len = k - j + 1
        print("new_len:%d, j:%d, k:%d str:%s" % (new_len, j, k, str1[j:k+1]))
        if (new_len > max_len):
          max_len = new_len
          ans = str1[j:k+1]
  for i in range(n):
    print (dp[i])
  print ("ans:%s" % (ans))
  return ans

def bruteForce(str1):
  if (str1 == str1[::-1]):
    return str1
  n = len(str1)
  max_len = 1
  ans = ""
  for i in range(n - 1):
    for j in range(i + 1, n):
      new_len = j - i + 1
      if (new_len > max_len and str1[i:j+1] == str1[i:j+1][::-1]):
        max_len = new_len
        ans = str1[i:j+1]
  return ans

def random_str(slen=10):
    seed = "abcd"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)

if __name__ == "__main__":
  for _ in range(1000):
    ran_str = random_str()
    print ("ran_str:%s" % (ran_str))
    ans1 = longestPalindrome(ran_str)
    ans2 = bruteForce(ran_str)
    if not (ans1 == ans2):
      print ("Error!! ans1:%s ans2:%s" % (ans1, ans2))
      break