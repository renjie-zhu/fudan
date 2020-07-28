#!/home/xnli/tools/python3.6/bin/python3.6
#!/usr/bin/python3
import random
import string
import sys

def reverseIntNum(num):
  num_ans = 0
  while (num):
    pop = num  % 10
    num = num // 10
    min_value = -sys.maxsize - 1
    if (num_ans > sys.maxsize // 10 or (num_ans == sys.maxsize // 10 and pop > 7)):
      print ("overflow")
      return 0
    if (num_ans < min_value // 10 or (num_ans == min_value // 10 and pop < -8)):
      print ("overflow")
      return 0
    num_ans = num_ans * 10 + pop
  return num_ans

def bf_for_test(num):
  str1 = str(num)
  str2 = str1[::-1]
  num  = int(str2)
  return num

def random_str(slen=10):
    seed = "0123456789"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)

if __name__ == "__main__":
  for _ in range(1000):
    num_ran = int(random_str())
    num_golden = bf_for_test(num_ran)
    num_check  = reverseIntNum(num_ran)
    print("   num_ran:%s\nnum_golden:%s\n num_check:%s" % (num_ran, num_golden, num_check))
    if (num_golden != num_check):
      print("Error!")
      break