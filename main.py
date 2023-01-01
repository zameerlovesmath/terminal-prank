import os
prompt = input("Terminal name: ")
lyric = 0
os.system("clear")
while True:
  command = input(prompt+" ")
  if lyric == 0:
    print("Never gonna give you up")
    lyric += 1
  command = input(prompt+" ")
  if lyric == 1:
    print("Never gonna let you down")
    lyric += 1
  command = input(prompt+" ")
  if lyric == 2:
    print("Never gonna run around and desert you")
    lyric += 1
  command = input(prompt+" ")
  if lyric == 3:
    print("Never gonna make you cry")
    lyric += 1
  command = input(prompt+" ")
  if lyric == 4:
    print("Never gonna say goodbye")
    lyric += 1
  command = input(prompt+" ")
  if lyric == 5:
    print("Never gonna tell a lie and hurt you")
    command = input(prompt+" ")
    lyric = 0
