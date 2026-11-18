from rich.console import Console
from InquirerPy import inquirer
from urllib.parse import urlparse
from core import dowload,getinfo
import time
console = Console()
run = True
while run:
    menu = inquirer.select(
        message="Select an option for downloads:",
        choices=[
            "Single Download",
            "Multiples Downloads",
            "SOON OR SOME BS",
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
            title,channel,upload_date,filesize_approx,*shit = getinfo(sndwn)
            console.print(f"[bold black]Title:{title}[/bold black]\n [bold white]Channel:{channel}[/bold white]\n [bold black]Upload Date:{upload_date}[/bold black]")
            crv = inquirer.confirm(
                message="Is this your video"
            ).execute()
            if crv:
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
                if quality == "Best Video,Audio":
                    try:
                        dowload(sndwn,"best")
                        console.print(f"[bold green]Download Complete![/bold green]")
                        time.sleep(1)
                    except Exception as e:
                        console.print(f"[bold red]The Download Failed[/bold red]")
                elif quality == "Worst Video,Audio":
                    try:
                        dowload(sndwn,"worstvideo+worstaudio")
                        console.print(f"[bold green]Download Complete![/bold green]")
                        time.sleep(1)
                    except Exception as e:
                        console.print(f"[bold red]The Download Failed[/bold red]")
                elif quality == "Best Video/No Audio":
                    try:
                        dowload(sndwn,"bestvideo")
                        console.print(f"[bold green]Download Complete![/bold green]")
                        time.sleep(1)
                    except Exception as e:
                        console.print(f"[bold red]The Download Failed[/bold red]")
                elif quality == "Worst Video/No Audio":
                    try:
                        dowload(sndwn,"worstvideo")
                        console.print(f"[bold green]Download Complete![/bold green]")
                        time.sleep(1)
                    except Exception as e:
                        console.print(f"[bold red]The Download Failed[/bold red]")
                elif quality == "Best Audio/No Video":
                    try:
                        dowload(sndwn,"bestaudio")
                        console.print(f"[bold green]Download Complete![/bold green]")
                        time.sleep(1)
                    except Exception as e:
                        console.print(f"[bold red]The Download Failed[/bold red]")
                elif quality == "Worst Audio/No Video":
                    try:
                        dowload(sndwn,"worstaudio")
                        console.print(f"[bold green]Download Complete![/bold green]")
                        time.sleep(1)
                    except Exception as e:
                        console.print(f"[bold red]The Download Failed[/bold red]")
            else:
                time.sleep(1)
    elif menu == "Exit":
        run = False