
## Flask API for running the Optim Group Formation

## Installing instructions

To get the App running we need to install some python packages in a virtual environment. These packages are collected in the file ```requirements.txt```. First, clone the repo and then follow the next steps to get those requirements ready in your local computer.

For this case I just call the new environment as ```env```

## Install Requirements for Python Anaconda Users

If you are an Anaconda user follow these steps. 

cd into src folder and:

- **Step 1: Create a new environment**

```conda create -n env```

- **Step 2: Activate the new environment**

```conda activate env```

- **Step 3: Install pip**

```conda install pip```

- **Step 4: Install all the virtualenv packages**

```pip install -r requirements.txt```

## Install Requirements for Python

If you are a Python user without an Anaconda distribution, follow these steps. 

cd into src folder and:

- **Step 1: Create a new environment**

```py -m venv env``` (Windows)

```python3 -m venv env``` (Unix/macOS)

- **Step 2: Activate the new environment**

```.\env\Scripts\activate.bat``` (Windows)

```source env/bin/activate``` (Unix/macOS)

- **Step 3: Install all the virtualenv packages**

```pip install -r requirements.txt```

Once you have installed all the requirements and you are in the environment you can run the app typing: ```flask run```

## Example: How to retrieve data from RStudio

```{r, eval=FALSE}
library(httr)
url <- "http://127.0.0.1:5000/OGF"
body_list <- list("a" = matrix(rbinom(100, 1, 0.5), 10, 10), "C" = 2, "NM" = 5)
response <- httr::content(httr::POST(url = url, body = body_list, encode = "json"))
results$decisons
results$objective_value
```

<br>
<br>
