import yt_dlp
def dowload(link,format):
    options = {
        "quiet":True,
        "no_warnings":True,
        "format":format
    }
    with yt_dlp.YoutubeDL(options)as yt:
        yt.download([link])

def getinfo(link):
    options = {
        "quiet":True,
        "no_warnings":True
    }
    with yt_dlp.YoutubeDL(options)as yt:
        info = yt.extract_info(link,download=False)
        return info.get("title") or "Unknown",info.get("channel") or "Unknown",info.get("upload_date") or "Unknown",info.get("filesize_approx") or "Unknown"