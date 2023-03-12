from typing import List;

def signed_area(data: List[float])->float:
  sum = 0
  j = len(data)-2
  for i in range(0, len(data), 2):
    sum += (data[i]-data[j])*(data[i+1]+data[j+1])
    j = i
  return sum

def get_sign(sum):
  if sum>0: return "CW"
  elif sum==0: return "Zero"
  else: return "CCW"

def area(x0,y0, x1,y1, x2,y2):
  return (y1-y0)*(x2-x1) - (x1-x0)*(y2-y1)