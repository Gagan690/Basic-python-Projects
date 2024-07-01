from pytube import YouTube

YouTube('https://youtube.com/shorts/weH4fGjm08Y?si=ZLnRsxJ0MLdpgPs7').streams.first().download()
print("Your Video Has Been Download")
