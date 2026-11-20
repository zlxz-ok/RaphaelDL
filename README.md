# RaphaelDL

## What is RaphaelDL?

RaphaelDL is a command-line video downloader that supports multiple platforms through [yt-dlp](https://github.com/yt-dlp/yt-dlp) as its backend.

It provides a simple interface for downloading videos, selecting formats and quality, and managing download locations.

## Features

- **Single Download:** Download content from a single URL and choose the desired quality before downloading.
- **Multiple Downloads:** Add as many URLs as you want and select the desired quality. If one download fails, RaphaelDL continues with the remaining URLs.
- **Quick Download:** Download content from a single URL without selecting a quality. Uses `bestvideo*+bestaudio/best` as its default format selector.
- **Configuration:** Set a custom download folder. You can also use SMB network storage if it is mounted on your system.

## Requirements

- Python
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [InquirerPy](https://github.com/kazhala/InquirerPy)
- [Rich](https://github.com/Textualize/rich)
- **FFmpeg** (recommended for merging separate video and audio streams)

## Third-Party Libraries

RaphaelDL uses the following open-source projects:

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) — Unlicense
- [InquirerPy](https://github.com/kazhala/InquirerPy) — MIT License
- [Rich](https://github.com/Textualize/rich) — MIT License

See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for more information about their licenses.

## Configuration

RaphaelDL allows you to choose a custom folder for downloaded files.

On Linux, you can also use an SMB network share by mounting it as a local directory.

## Downloads & Installation

RaphaelDL is distributed through [pipx](https://pipx.pypa.io/).

**Requirements:** Python 3.11+, pipx and FFmpeg (recommended).

### Linux

Install pipx:

```bash
# Fedora
sudo dnf install pipx

# Ubuntu
sudo apt update && sudo apt install pipx
```

Configure and install RaphaelDL:

```bash
pipx ensurepath
pipx install git+https://github.com/zlxz-ok/RaphaelDL.git
```

Restart your terminal, then run:

```bash
rpdl
```

### Windows

Open PowerShell:

```powershell
py -m pip install --user pipx
py -m pipx ensurepath
```

Restart PowerShell, then install and run:

```powershell
pipx install git+https://github.com/zlxz-ok/RaphaelDL.git
rpdl
```

### Uninstall

On either platform:

```bash
pipx uninstall raphaeldl
```

## SMB Network Storage Setup (Linux)

RaphaelDL supports downloading files directly to an SMB network share mounted on your Linux system.

### 1. Install CIFS utilities

On Fedora:

```bash
sudo dnf install cifs-utils
```

On Debian/Ubuntu:

```bash
sudo apt install cifs-utils
```

### 2. Create a mount point

Create a directory where the network share will be accessible:

```bash
sudo mkdir -p /mnt/raphaeldl
```

### 3. Mount the SMB share

Replace the placeholders with your server information:

```bash
sudo mount -t cifs //SERVER_IP/SHARE_NAME /mnt/raphaeldl -o username=SMB_USER,uid=$(id -u),gid=$(id -g)
```

You will be prompted for your SMB password.

### 4. Verify the connection

Check that the shared files are accessible:

```bash
ls /mnt/raphaeldl
```

If the connection is successful, the contents of your SMB share should appear.

### 5. Configure RaphaelDL

Open RaphaelDL and navigate to **Config → Custom Folder**.

Enter the mount point path:

```text
/mnt/raphaeldl
```

**Important:** The SMB share must be mounted before starting RaphaelDL.

### 6. Unmount the share

When you no longer need the connection:

```bash
sudo umount /mnt/raphaeldl
```

**Note:** This is a temporary mount. It must be mounted again after restarting the system. Automatic mounting can be configured using `/etc/fstab`.

## License

RaphaelDL is licensed under the [MIT License](LICENSE).

Third-party libraries retain their respective licenses. See [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for details.
