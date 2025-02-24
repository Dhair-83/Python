def mlg(lst):
    result={}
    for item in lst:
      result[item[0]]=item[1:]
    return result
student=[[1,'sui',31],[2,'messi',32],[3,'limca',33]]
print("original list:")
print(student)
print("Converted list:")
print(mlg(student))