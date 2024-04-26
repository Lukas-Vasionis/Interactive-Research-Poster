# Proof of concept: Interactive research poster

## Current ways to share
Currently scientists and students share most of their ideas in three ways:
- papers: which are very informative, therefore, consume a lot of time and energy to understand and is easily sharable
- presentations: which are moderately informative, therefore, is quicker to understand, but requires to bypass a lot of obstacles to share it.
- posters: which are less informative, therefore, quick to comprehend, however, the sharability is very complicated. 

|| Compression of Ideas | Time to Understand | Struggle to Understand | Sharing Opportunities |
|----------|----------|----------|----------|----------|
|Paper| $\color{green}{\textsf{Least}}$| $\color{red}{\textsf{Large}}$ | $\color{red}{\textsf{Large}}$ |$\color{green}{\textsf{Wide}}$ |
|Presentation| $\color{olive}{\textsf{Medium}}$ | $\color{olive}{\textsf{Medium}}$ | $\color{olive}{\textsf{Medium}}$ |$\color{olive}{\textsf{Restricted}}$ |
|Poster| $\color{red}{\textsf{Large}}$ | $\color{green}{\textsf{Least}}$ | $\color{green}{\textsf{Least}}$ |$\color{red}{\textsf{Very Restricted}}$ |

## New way to introduce complex data
The current format of paper scientific posters present ideas the quickest. However, its almost impossible to bring it to the colleagues on other labs. The paper posters usualy end up on a lab's wall and serves almost no purpose for global scientific process. 

It also has strong limmitations in expressing the complex data - a 2D physical poster can't present multi-dimensionsional data. Sometimes, a single idea of research must be expressed in multiple graphs, animations, 3D graphs or videos and 2D physical posters can't do that.

Therefore, as we come to the 2nd decade of 21st century it is time to upgrade this Atomic age media with interactivity and accesabilty. 

This repository demonstrates some concepts of interactive poster which can overcome the problem of sharing complex ideas in quick and attractive manner. The following interactive poster describes a mock reseach paper, and uses some simple widgets to expand data visualisation capacity. 
It also demonstrates potential to design your poster with predefined great-looking elements like containers for chapters, standartized text options and custom background images. Finally, streamlit framework provides infrastructure to share your interactive poster as a webpage for free. This provides a free hub to share your results with global community of science. 

You may find our example here: https://goposteryourself.streamlit.app/, or by loading this poster locally.

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
