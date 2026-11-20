from rich.console import Console
from InquirerPy import inquirer
from urllib.parse import urlparse
from core import dowload,getinfo
from pathlib import Path
import time,json
console = Console()
def squality():
    quality = inquirer.select(
        message="Select the quality you want/it may fail sometimes:",
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
def furl(quality,urls,cfolder):
    if quality == "Best Video,Audio":
     try:
        dowload(urls,"best",cfolder)
        console.print(f"[bold green]Download Complete![/bold green]")
        time.sleep(1)
     except Exception as e:
        console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Worst Video,Audio":
        try:
            dowload(urls,"worstvideo+worstaudio",cfolder)
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
             console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Best Video/No Audio":
        try:
            dowload(urls,"bestvideo",cfolder)
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Worst Video/No Audio":
        try:
            dowload(urls,"worstvideo",cfolder)
            console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Best Audio/No Video":
        try:
            askformat = inquirer.select(
                message="What format you want/it may fails sometimes?:",
                choices=[
                    "M4A",
                    "WEBM"
                ]
            ).execute()
            if askformat == "M4A":
                dowload(urls,"bestaudio[ext=m4a]/bestaudio",cfolder)
                console.print(f"[bold green]Download Complete![/bold green]")
            elif askformat == "WEBM":
                dowload(urls,"bestaudio[ext=webm]/bestaudio",cfolder)
                console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
    elif quality == "Worst Audio/No Video":
        try:
            if askformat == "M4A":
                dowload(urls,"worstaudio[ext=m4a]/worstaudio",cfolder)
                console.print(f"[bold green]Download Complete![/bold green]")
            elif askformat == "WEBM":
                dowload(urls,"worstaudio[ext=webm]/worstaudio",cfolder)
                console.print(f"[bold green]Download Complete![/bold green]")
            time.sleep(1)
        except Exception as e:
            console.print(f"[bold red]The Download Failed[/bold red]")
def main():
    run = True
    try:
        with open ("cfg.json","r") as config:
            data = json.load(config)
            cfolder = data["folder"]
    except FileNotFoundError:
        cfolder = str(Path.home() / "Downloads")
        with open ("cfg.json","w") as config:
            json.dump({"folder":cfolder},config)
    while run:
        menu = inquirer.select(
            message="Select an option for downloads:",
            choices=[
                "Single Download",
                "Multiples Downloads",
                "Quick Download",
                "Config",
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
                     message="Is this your video:"
                 ).execute()
                 if crv:
                     quality = squality()
                     furl(quality,sndwn,cfolder)
                else:
                    pass
        elif menu == "Multiples Downloads":
            links = []
            #mlpdwn = multiple downloads i think
            while True:
             mlpdwn = inquirer.text(
                 message="URL of the video:"
             ).execute()
             mparsed = urlparse(mlpdwn)
             if mparsed.scheme not in ("https","http") or not mparsed.netloc:
                 console.print(f"[bold red]Insert a correct URL please[/bold red]")
             else:
                 links.append(mlpdwn)
             cmlpdwn = inquirer.confirm(
                 message="Add anothern url?:"
             ).execute()
             if not cmlpdwn:
                 break
            qualitys = squality()
            for link in links:
             furl(qualitys,link,cfolder)
        elif menu == "Config":
            mconfig = inquirer.select(
                message="Select a config:",
                choices=[
                    "Custom Folder",
                ]
            ).execute()
            if mconfig == "Custom Folder":
                path = inquirer.text(
                    message="Insert folder:"
                ).execute()
                if path == "":
                    console.print(f"[bold red]No Folder Found![/bold red]")
                path = Path(path).expanduser()
                if path.is_dir():
                    with open ("cfg.json","w") as config:
                        json.dump({"folder":str(path)},config)
                    with open ("cfg.json","r") as config:
                        data = json.load(config)
                        cfolder = data["folder"]
                else:
                    console.print(f"[bold red]No Folder Found![/bold red]")
        elif menu == "Quick Download":
            qkdwn = inquirer.text(
                message="URL of the video:"
            ).execute()
            qparsed = urlparse(qkdwn)
            if qparsed.scheme not in ("https", "http") or not qparsed.netloc:
                console.print("[bold red]Insert a correct URL please[/bold red]")
            else:
                try:
                    dowload(qkdwn, "bestvideo*+bestaudio/best", cfolder)
                    console.print("[bold green]Download Complete![/bold green]")
                except Exception as e:
                    console.print("[bold red]The Download Failed[/bold red]")
        elif menu == "Exit":
            run = False

if __name__ == "__main__":
    main()