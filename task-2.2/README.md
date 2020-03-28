## CHaRLy-v2 Instrctions

First off thank you for you time in taking the task! We really do appreciate it, and every participant is important to the study.

What follows will be instructions for running this task on your local machine. Note that some of the instructions might not work exactly as written for your computer, but as a guiding principle, you should run this script however you run normal python code.

### TLDR of commands to run the task


```
pip install -r stable-req.txt
python runner.py
```

### Step 1: Setting up a python environment

Prerequesities for running this task are python3 and pip. That is all.

As a first step, you will need to install all the packages in stable-req.txt. This can be done with the following command:

```pip install -r stable-req.txt```

If that doesn't work, you may need to run it with `pip3` instead of `pip`. Note that this step is probably most prone to errors, so if you see red that is ok! As long as you have psychopy installed - check this by running `pip install psychopy` - you should be good to go.

### Step 2: Running the task

The following command will run the task:

```python runner.py```

This will open a full screen window with the task. Note if your default is python2, you will need to use `python3` instead of `python`.

### Step 3: Saving the data

Your data from the task will now appear in the data folder. It will have a file name along the lines of `subj_1.json`, though the exact number might be different. You should send this file to amoghaddassi@berkeley.edu (or if someone else gave you the task, just send it to them).



