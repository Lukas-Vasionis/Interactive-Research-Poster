# Proof of concept: Interactive research poster
The current format of paper scientific posters present ideas the quickest. However, its almost impossible to bring it to the colleagues on other labs. The paper posters usualy end up on a lab's wall and serves almost no purpose for global scientific process. 

It also has strong limmitations in expressing the complex data - a 2D physical poster can't present multi-dimensionsional data. Sometimes, a single idea of research must be expressed in multiple graphs, animations, 3D graphs or videos and 2D physical posters can't do that.

Therefore, as we come to an epoch of complex data, it is time to upgrade this post-war media with interactivity and accesabilty.

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

This repository demonstrates some concepts of interactive poster which can overcome the problem of sharing complex ideas in quick and attractive manner. The following interactive poster describes a mock reseach paper, and uses some simple widgets to expand data visualisation capacity. 
It also demonstrates potential to design your poster with predefined great-looking elements like containers for chapters, standartized text options and custom background images. Finally, streamlit framework provides infrastructure to share your interactive poster as a webpage for free. This provides a free hub to share your results with global community of science. 

You may find our example here: https://goposteryourself.streamlit.app/, or by loading this poster locally.

![Page screen shot](https://github.com/Lukas-Vasionis/posters/blob/master/img/intro_scrshot.png?raw=True)

## Local Setup
> **Note:** All commands below assume you’re working in a Bash (or similar) terminal. <br><br>
For `windows` users I strongly 
recommend using `IDE`, like `PyCharm` - it smooths over most differences between windows and linux. In such case, use
terminal within PyCharm.

Follow these steps to clone, install, and run the Interactive Research Poster on your machine.

### Prerequisites

Make sure you have the following installed:

- **Python 3.12** (or later)  
- **Poetry** (for dependency management)  
- **Git**  

> **Tip:** You can verify your installations by running:
> ```bash
> python --version
> poetry --version
> git --version
> ```

---

### 1. Clone the Repository
```bash
git clone https://github.com/Lukas-Vasionis/Interactive-Research-Poster.git
cd Interactive-Research-Poster
```

### 2. Install Poetry (if needed)
If you don’t already have Poetry:
```bash
pip install --user poetry
```
>Note: On some systems you may need to add Poetry to your PATH. After installation, restart your terminal or follow Poetry’s post-install instructions.

### 3. Create & Activate the Virtual Environment
Inside the project root (`Interactive-Research-Poster`):
```bash
cd Interactive-Research-Poster
poetry install --no-root
```
- This command will:
    1. Create a new virtual environment.
    1. Install all dependencies listed in pyproject.toml.
    1. Skip installing the package itself (so you can make local edits).

### 4. Run the App
Start the Streamlit application:

```bash
poetry run streamlit run main.py
```
- Once ready, Streamlit will print a local URL (e.g. http://localhost:8501).
- Your default browser should open automatically; if it doesn’t, copy-and-paste that URL into your browser.