user_input=input("File name: ").lower().strip()
if ".git" in user_input:
      print("imge/gif")
elif ".jpg" in user_input or ".jpeg" in user_input:
      print("imge/jpeg")
elif ".png" in user_input:
      print("imge/png")
elif if ".pdf" in user_input:
      print("application/pdf")
else:
      print("application/octet-stream")

