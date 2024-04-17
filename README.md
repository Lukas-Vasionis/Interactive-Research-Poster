## Proof of concept: Interactive research poster
Currently scientists and students share most of their ideas in three ways:
- scientific papers: which are very informative, is easily accessable, yet consume a lot of time to understand
- presentations: which are moderately informative, has limmited accessability, consume less time to understand
- scientific posters: which are less informative, usualy has very limmited accessability, consume least time to understand

The current format of paper scientific posters present ideas in a quickes manner of all three. However, its almost impossible for consumer to bring it to the colleagues in a lab and has strong limmitations in expressing complex data. 
The paper posters usualy end up on a wall of presenting scientist's wall and serves no purpose for scientific community. It also fails to pressent data with multiple dimensions,
or key points that requirere two different graphs of the same data, or more complex data visualisations like videos. All of theese limitations are overcomed with digital and interactive versions of paper posters. 

This repository demonstrates some concepts of interactive poster which can overcome the problem of sharing complex ideas within the science community. The interactive poster describes a mock reseach paper, and uses some simple widgets to expand the visualisation potential its data. 
It also demonstrates potential to design your poster with predefined great-looking elements like containers, standartized text options and custom background images. Finally, the used streamlit framework provides infrastructure to share your 
interactive poster as a webpage for free. You may find our example here: https://goposteryourself.streamlit.app/, or by loading this poster locally.

![Page screen shot](https://github.com/Lukas-Vasionis/posters/blob/master/img/intro_scrshot.png?raw=True)

## Loading locally
### Prerequisites: 
To load the poster locally, one must install these tools

- Python 3.11
- Git

### Installation and execution
1) Clone this repo to your computer.
```
git clone https://github.com/Lukas-Vasionis/posters.git
```
2) Create local environment
3) Install packages with requirements file:
```
pip install -r requirements.txt
```
4) Execute the main.py file with streamlit:
```
streamlit run ./main.py 
```
At this point your browser should open a tab with this app. If not, click the hyperlink in the output of your terminal.
