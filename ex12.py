a = [1,1,1,22,67,56,"apple","apple","banana","Besiek"]
b = []
def list_dupli():
    for x in a:
        b.append(x)
list_dupli()
print(list(set(b)))