#!/home/xnli/tools/python3.6/bin/python3.6
#!/usr/bin/python3
import random
import string
"""
ex.    maojqpeakkoqcjk , num_rows = 3
    ==>m   q   k   c ==> mqkcajpakqjoeok
       a j p a k q j 
       o   e   o   k
"""
def strConvertZstr(str1, num_rows):
  num_rows = min(num_rows, len(str1))
  str_arr = [[""] for _ in range(num_rows)]
  cur_row = 0
  going_down = False
  for i in range(len(str1)):
    str_arr[cur_row] += str1[i]
    if (cur_row == 0 or cur_row == num_rows - 1):
      going_down = not going_down
    cur_row += 1 if going_down else -1

  for i in range(1, num_rows):
    str_arr[0] += str_arr[i]
  return str_arr[0]

def random_str(slen=15):
    seed = "abcdefghijklmnopq"
    sa = []
    for i in range(slen):
      sa.append(random.choice(seed))
    return ''.join(sa)

if __name__ == "__main__":
  ran_str = random_str()
  str_ans = ''.join(strConvertZstr(ran_str, 3))
  print ("ran_str:%s\nstr_ans:%s" % (ran_str, str_ans))