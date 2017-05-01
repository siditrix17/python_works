from __future__ import unicode_literals
import youtube_dl
import os

def videoinfo(e):
	ydl_opts={}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	 meta=ydl.extract_info(e,download=False)



	print 'upload date : %s' %(meta['upload_date'])
        print 'uploader    : %s' %(meta['uploader'])
	print 'views       : %d' %(meta['view_count'])
	print 'likes       : %d' %(meta['like_count'])
	print 'dislikes    : %d' %(meta['dislike_count'])
	print 'id          : %s' %(meta['id'])
	print 'format      : %s' %(meta['format'])
	print 'duration    : %s' %(meta['duration'])
	print 'title       : %s' %(meta['title'])
	print 'description : %s' %(meta['description'])
	print'\n'
	opt=raw_input("wanna download now or exit----------- \n y--YES \n           e--EXIT:")




def downinfo(vi):
	ydl_opts={}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	 ydl.download(vi)


def download():
	print'--creating playlist------'
 	vi=[]
 	no=raw_input('enter no of videos to download:')
 	no=int(no)
 	for i in range(no):
		qe=raw_input("enter video's address:-")
		vi.append(qe)

 	downinfo(vi) 
 




print'----------youtube downloader---siditrix[v1.0]---------------'
print'\n'
print'download or know about a video:-'
ch=raw_input("enter your choice ..--d for download or --i for info:-")
if (ch=='d'):
 download() 
 
elif(ch=='i'):
	eh=raw_input('enter video address:-')
	videoinfo(eh)
	print'wanna download now!!'
	pk=raw_input("--y for yes --n for no:-")
	if (pk=='y'):
		download()
	else:
		exit()




