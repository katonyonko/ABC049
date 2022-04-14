from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="049"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc065_a".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  import sys
  sys.setrecursionlimit(1000000)
  S=input()
  memo=[-1]*(len(S)+1)
  memo[0]=1
  def rec(s):
    if memo[s]>=0: return memo[s]
    ans=0
    if s>=5 and (S[-s:-s+5]=='dream' or S[-s:-s+5]=='erase'):
      ans=max(ans,rec(s-5))
    if s>=6 and S[-s:-s+6]=='eraser':
      ans=max(ans,rec(s-6))
    if s>=7 and S[-s:-s+7]=='dreamer':
      ans=max(ans,rec(s-7))
    memo[s]=ans
    return ans
  if rec(len(S))==0: print('NO')
  else: print('YES')
  """ここから上にコードを記述"""

  print(test_case[__+1])