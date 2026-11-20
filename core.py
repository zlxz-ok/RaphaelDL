import yt_dlp
from pathlib import Path
def dowload(link,format,cfolder):
    options = {
        "quiet":True,
        "no_warnings":True,
        "format":format,
        "outtmpl":str(Path(cfolder) / "%(title)s.%(ext)s")
    }
    with yt_dlp.YoutubeDL(options)as yt:
        yt.download([link])

def getinfo(link):
    options = {
        "quiet":True,
        "no_warnings":True
    }
    try:
       with yt_dlp.YoutubeDL(options)as yt:
            info = yt.extract_info(link,download=False)
            return True, info.get("title") or "Unknown",info.get("channel") or "Unknown",info.get("upload_date") or "Unknown",info.get("filesize_approx") or "Unknown"
    except Exception as e:
        return False, str(e),None,None,None