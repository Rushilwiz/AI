# Rushil Umaretiya
# Sept 8, 2020

# Here is my comment!!!! Hello!!

# Warmup-1
def sleep_in(weekday, vacation):
   return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
   return a_smile == b_smile

def sum_double(a, b):
   return (a+b)*2 if a == b else a+b

def diff21(n):
   return abs(21-n)*2 if n > 21 else abs(21-n)

def parrot_trouble(talking, hour):
   return talking and (hour < 7 or hour > 20)

def makes10(a, b):
   return True if a == 10 or b == 10 else a + b == 10

def near_hundred(n):
   return abs(100-n) <= 10 or abs(200-n) <= 10

def pos_neg(a, b, negative):
   return a < 0 and b < 0 if negative else (a < 0 and b > 0) or (a > 0 and b < 0)

# String-1
def hello_name(name):
   return "Hello " + name + "!"

def make_abba(a, b):
   return a+b*2+a

def make_tags(tag, word):
   return "<"+tag+">"+word+"</"+tag+">"

def make_out_word(out, word):
   return out[:len(out)//2]+word+out[len(out)//2:]

def extra_end(str):
   return str[-2:]+str[-2:]+str[-2:]

def first_two(str):
   return str if len(str)<2 else str[:2]

def first_half(str):
   return str[:len(str)//2]

def without_end(str):
   return str[1:-1]

# List-1
def first_last6(nums):
   return str(nums[0]) == '6' or str(nums[len(nums)-1]) == '6'

def same_first_last(nums):
   return False if len(nums) < 1 else nums[0] == nums[len(nums)-1]

def make_pi(n):
   return [3,1,4,1,5,9,2,6,5,3,5,8,9,7][:n]

def common_end(a, b):
   return a[len(a)-1] == b[len(b)-1] or a[0] == b[0]

def sum3(nums):
   return sum(nums)

def rotate_left3(nums):
   return nums[1:]+nums[:1]

def reverse3(nums):
   return [i for i in reversed(nums)]

def max_end3(nums):
   return [max(nums[0],nums[len(nums)-1])]*len(nums)

# Logic-1
def cigar_party(cigars, is_weekend):
   return not (cigars < 40 or (not is_weekend and cigars > 60))

def date_fashion(you, date):
   return 0 if you <= 2 or date <= 2 else 2 if you >= 8 or date >= 8 else 1

def squirrel_play(temp, is_summer):
   return temp >= 60 and ((is_summer and temp <= 100) or (not is_summer and temp <= 90))

def caught_speeding(speed, is_birthday):
   return 0 if speed <= 60 or (is_birthday and speed <= 65) else 1 if speed <= 80 or (is_birthday and speed <= 85) else 2

def sorta_sum(a, b):
   return 20 if a+b in range(10,20) else a+b

def alarm_clock(day, vacation):
   return "7:00" if day in range(1,6) and not vacation else "10:00" if not vacation or day in range(1,6) else "off"

def love6(a, b):
   return a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6

def in1to10(n, outside_mode):
   return n in range (1,11) if not outside_mode else n <= 1 or n >= 10
