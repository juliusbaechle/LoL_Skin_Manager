# LoL_Skin_Manager
Enables pre-game selection of any champion skin in League of Legends. Only affects client side.

<img src="docs/proof_of_concept.png" alt="proof of concept: Ahri - KDA All Out - Emerald">

Usage: 
- Download code and dependencies:
  > Clone this github repository  
  > Download latest Ritobin: https://github.com/moonshadow565/ritobin  
  > Download latest CSLOL-Manager: https://github.com/LeagueToolkit/cslol-manager  
  > Adapt paths in src/config.json
- Create skin:  
  > If necessary, download and install python: https://www.python.org/downloads/  
  > Adapt champ and skin number in main.py (f.e. Ahri 37)  
  > Run main.py (double click)
- Open CSLOL-Manager:
  > Your created skin should appear in the list  
  > Select created skin  
  > Click "Run"
- Join game with base skin and have fun :)
<br>  

How to find the skin number?
- Comment out line "shutil.rmtree("..\\orig\\")" and run skript
- Open "orig\\\<champ>\assets\characters\\\<champ>\hud" to find the skin series
- Open "orig\\\<champ>\assets\characters\\\<champ>\skins\skin\<nbr>" to find the chroma
<br>  

Todos:
- Selection of skins by visualization or at least name (currently by number)
- Possibly trigger a resource reload at runtime
