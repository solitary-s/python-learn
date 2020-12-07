
def main():
  try:
    with open('cat_200_300.jpg', 'rb') as fs1:
      data = fs1.read()
      print(type(data))
    with open('cat1.jpg', 'wb') as fs2:
      fs2.write(data)
  except FileNotFoundError as e:
    print(e)
  
if __name__ == '__main__':
  main()