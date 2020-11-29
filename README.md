## Original tribute
alexbel/conky
## Looks like:
![Sample](sample.png)

## Installation
- Clone repo `git clone https://github.com/mesenev/conky.git ~/conky`
- Copy content of result & scripts folder to ~/.config/conky
- chmod +x ~/.config/conky/netstat.sh
- Add `python .config/conky/launcher.py &` to your `.xinitrc` or find another way execute launcher.py on start.
- Change stuff to fit your system & needs

### Conky versions
- Use `master` branch for conky >= 1.10.0

### Dependencies
Required:  
  - curl
  - ss
  - acpi
  - sensors
