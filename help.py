from rich.console import Console
from InquirerPy import inquirer
from urllib.parse import urlparse
from core import dowload,getinfo
import time
console = Console()
run = True
def squality():
    quality = inquirer.select(
        message="Select the quality you want/it may fail sometimes",
        choices=[
        "Best Video,Audio",
        "Worst Video,Audio",
        "Best Video/No Audio",
        "Worst Video/No Audio",
        "Best Audio/No Video",
        "Worst Audio/No Video"
        ]
    ).execute()
    return quality
def furl(quality,urls):
    if quality == "Best Video,Audio":
     try:
        dowload(urls,"best")
        console.print(f"[bold green]Download Complete![/bold green]")
        time.sleep(1)
     except Exception as e:
        console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Worst Video,Audio":
        try:
            dowload(urls,"worstvideo+worstaudio")
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
             console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Best Video/No Audio":
        try:
            dowload(urls,"bestvideo")
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Worst Video/No Audio":
        try:
            dowload(urls,"worstvideo")
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Best Audio/No Video":
        try:
            dowload(urls,"bestaudio")
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Worst Audio/No Video":
        try:
            dowload(urls,"worstaudio")
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
while run:
    menu = inquirer.select(
        message="Select an option for downloads:",
        choices=[
            "Single Download",
            "Multiples Downloads",
            "Soon i think",
            "Configure SMB",
            "Exit"
        ]
    ).execute()
    if menu == "Single Download":
        #sndwn = SiNgle DoWNload
        sndwn = inquirer.text(
            message="URL of the video:"
        ).execute()
        parsed = urlparse(sndwn)
        if parsed.scheme not in ("https","http") or not parsed.netloc:
            console.print(f"[bold red]Insert a correct URL please[/bold red]")
        else:
            status,title,channel,upload_date,filesize_approx,*shit = getinfo(sndwn)
            if status:
             console.print(f"[bold black]Title:{title}[/bold black]\n [bold white]Channel:{channel}[/bold white]\n [bold black]Upload Date:{upload_date}[/bold black]")
             crv = inquirer.confirm(
                 message="Is this your video"
             ).execute()
             if crv:
                 quality = squality()
                 furl(quality,sndwn)
            else:
                pass
    elif menu == "Multiples Downloads":
        links = []
        #mlpdwn = multiple downloads i think
        while True:
         mlpdwn = inquirer.text(
             message="Insert your first link:"
         ).execute()
         parsed1 = urlparse(mlpdwn)
         if parsed1.scheme not in ("https","http") or not parsed1.netloc:
             console.print(f"[bold red]Insert a correct URL please[/bold red]")
         else:
             links.append(mlpdwn)
         cmlpdwn = inquirer.confirm(
             message="Add anothern url?"
         ).execute()
         if not cmlpdwn:
             break
        qualitys = squality()
        for link in links:
         furl(qualitys,link)
                 
    elif menu == "Exit":
        run = False