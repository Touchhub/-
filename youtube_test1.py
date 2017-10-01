from pytube import YouTube
from pprint import  pprint
yt_url=YouTube('https://www.youtube.com/watch?v=b57XVkLADaM')
#pprint(yt_url.get_videos())
#print(yt_url.filename)
yt_url.set_filename('my_firstvideo')
video=(yt_url.filter('mp4')[-1])
#video=yt_url.get('mp4','720p')
video.download('D:\Game')
print('all is done')
